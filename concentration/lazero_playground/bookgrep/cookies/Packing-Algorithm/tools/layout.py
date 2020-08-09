'''
Get feasible result based on minimizing overlap and relocating pieces
Several algorithms are achieved in this file
命名规范：类名全部大写、其他函数首字母小写、变量名全部小写
'''
from polygon import GeoFunc,PltFunc,getData
from sequence import BottomLeftFill
import pandas as pd
import json
from shapely.geometry import Polygon,Point,mapping,LineString
from interval import Interval

precision_error=0.000000001

class Beam():
    '''
    参考资料：A beam search implementation for the irregular shape packing problem 
    '''
    def __init__(self):
        pass

class Tabu():
    '''
    参考资料：Extended local search algorithm based on nonlinear programming for two-dimensional irregular strip packing problem
    '''
    def __init__(self):
        pass

class CuckooSearch():
    '''
    参考资料：2013 A new approach for sheet nesting problem using guided cuckoo search and pairwise clustering
    '''
    def __init__(self):
        pass

class FNS():
    '''
    参考资料：2004 Fast neighborhood search for two- and three-dimensional nesting problems
    概述：通过贪婪算法，分别在xy轴平移寻找轴上相交面积最小的位置
    待完成：旋转、需要依次采用水平移动/垂直移动/旋转、收缩的高度降低
    '''
    def __init__(self,polys):
        self.polys = polys
        self.width = 1500
        self.height = 999999999
        self.initial()
        self.main()

    def main(self):
        self.shrink()
        self.guidedLocalSearch()

        # while(True):
            # self.shrink()
            # self.guidedLocalSearch()
        
        self.showResult(current=True)
        
    # 获得初始解和判断角度位置  
    def initial(self):
        pp = BottomLeftFill(self.width,self.polys)
        self.height = pp.contain_height
        self.updatePolyList()
    
    # 计算所有形状和其他形状的 Overlap 以及是否没有重叠
    def updateOverlap(self):
        # 计算重叠情况
        self.overlap_pair=[[0]*len(self.cur_polys) for i in range(len(self.cur_polys))]
        self.overlap_each=[0 for i in range(len(self.cur_polys))]
        for i in range(0,len(self.cur_polys)-1):
            for j in range(i+1,len(self.cur_polys)):
                Pi=Polygon(self.cur_polys[i])
                Pj=Polygon(self.cur_polys[j])
                overlap_area=GeoFunc.computeInterArea(Pi.intersection(Pj))
                if overlap_area>precision_error:
                    self.overlap_pair[i][j]=self.overlap_pair[i][j]+overlap_area
                    self.overlap_pair[j][i]=self.overlap_pair[i][j]
                    self.overlap_each[i]=self.overlap_each[i]+overlap_area
                    self.overlap_each[j]=self.overlap_each[j]+overlap_area

        # 计算修正后的参考值，同时修正Phi
        max_miu_pair=0
        max_miu_pair_indx=[0,0]
        for i in range(0,len(self.cur_polys)):
            for j in range(0,len(self.cur_polys)):
                miu=self.overlap_pair[i][j]/(1+self.phi[i][j])
                self.miu_each[i]=self.miu_each[i]+miu
                if miu>max_miu_pair:
                    max_miu_pair_indx=[i,j]
        self.phi[max_miu_pair_indx[0]][max_miu_pair_indx[0]]+=1
                
        # 获得最大的Miu及其Index
        self.max_miu=0
        self.max_miu_index=-1
        for index,miu in enumerate(self.miu_each):
            if miu>self.max_miu:
                self.max_miu=miu
                self.max_miu_index=index

        # 更新是否重叠
        self.overlap=False
        for area in self.overlap_each:
            if area>0:
                self.overlap=True

    # 收缩宽度
    def shrink(self):
        self.new_height=self.height*0.95
        self.cur_polys=[]
        for poly in self.polys:
            top_index=GeoFunc.checkTop(poly)
            delta=self.new_height-poly[top_index][1]
            if delta>=0:
                self.cur_polys.append(GeoFunc.copyPoly(poly))
            else:
                self.cur_polys.append(GeoFunc.getSlide(poly,0,delta))
    
    # 展示最终结果
    def showResult(self,**kw):
        if "current" in kw and kw["current"]==True:
            for poly in self.cur_polys:
                PltFunc.addPolygonColor(poly)
            PltFunc.addLine([[0,self.new_height],[self.width,self.new_height]],color="blue")
        if "initial" in kw and kw["initial"]==True:
            for poly in self.polys:
                PltFunc.addPolygon(poly)
            PltFunc.addLine([[0,self.height],[self.width,self.height]],color="blue")
        PltFunc.showPlt()

    # 在水平或者垂直直线上寻找最优位置
    def slideNeighbor(self,poly,_type):
        self.break_points_list=[]
        if _type=="horizontal":
            # 分别四种情况
            self.getEdgeBreakPoint(self.horizontal_positive,self.target_horizontal_positive,_type,-1)
            self.getEdgeBreakPoint(self.horizontal_negative,self.target_horizontal_negative,_type,-1)
            self.getEdgeBreakPoint(self.horizontal_positive,self.target_horizontal_negative,_type,1)
            self.getEdgeBreakPoint(self.horizontal_negative,self.target_horizontal_positive,_type,1)
            self.break_points_list=sorted(self.break_points_list,key=lambda x:(x[0]))
            print("排序结果:\n",self.break_points_list)
            self.pltArea()
        
        if _type=="vertical":
            print("进行垂直计算")
            # for edge in self.horizontal_positive:
                # for target_edge in self.target_horizontal_positive:
                    # self.getBreakPoints(target_edge,edge,_type)
    
    # 输入Positive和Negative的边，返回Break Point List
    def getEdgeBreakPoint(self,edges,target_edges,_type,sign):
        for edge in self.horizontal_positive:
            for target_edge in self.target_horizontal_positive:
                res=self.getBreakPointsList(target_edge,edge,_type)
                if res==None:
                    continue
                # 特殊情况需要变负
                if sign==-1:
                    for ABC in res:
                        for i in range(1,4):
                            ABC[i]=-ABC[i]
                self.break_points_list.append(res[0])
                self.break_points_list.append(res[1])

    # 获得面积的徒刑
    def pltArea(self):
        A,B,C=0,0,0
        for i,coefficient in enumerate(self.break_points_list):
            print(coefficient)
            A=A+coefficient[1]
            B=A+coefficient[2]
            C=A+coefficient[3]
            if i>0:
                x=[self.break_points_list[i-1][0],coefficient[0]]
            else:
                x=[0,coefficient[0]]
            y0=self.getQuadratic(x[0],A,B,C)
            y1=self.getQuadratic(x[1],A,B,C)
            PltFunc.addLine([[x[0],y0],[x[1],y1]])
        PltFunc.showPlt()
    
    # 获得二次函数的最值
    def getQuadratic(self,x,A,B,C):
        return A*x*x+B*x+C

    # 获得水平或垂直平移的情况
    def getBreakPointsList(self,target_edge,edge,_type):
        if _type=="horizontal":
            # 两条直线四个组合计算
            break_points=[]
            self.getT(target_edge[0],edge,0,1,break_points)
            self.getT(target_edge[1],edge,0,1,break_points)
            self.getT(edge[0],target_edge,0,-1,break_points)
            self.getT(edge[1],target_edge,0,-1,break_points)
            # 必须是有两个交点       
            if len(break_points)<2:
                return 
            # 开始计算具体参数
            t1=min(break_points[0],break_points[1])
            t2=max(break_points[0],break_points[1])
            target_slide1=[[target_edge[0][0]+t1,target_edge[0][1]],[target_edge[1][0]+t1,target_edge[1][1]]] # 平移后的结果
            target_slide2=[[target_edge[0][0]+t2,target_edge[0][1]],[target_edge[1][0]+t2,target_edge[1][1]]] # 平移后的结果
            pt1=GeoFunc.intersection(target_slide1,edge) # 可能为Tuple
            pt2=GeoFunc.intersection(target_slide2,edge) # 可能为Tuple
            pt3=self.getHoriVerInter(pt1,target_slide2,0)
            # 计算A1 B1 C1
            ratio=(LineString([pt1,pt2]).length)/(t2-t1) # 两条边的比例
            sin_theta=abs(pt1[1]-pt2[1])/(LineString([pt1,pt2]).length) # 直线与水平的角度
            A1=0.5*ratio*sin_theta
            B1=-2*t1*A1
            C1=t1*t1*A1
            # 计算A2 B2 C2
            A2=0
            B2=abs(pt1[1]-pt2[1]) # 平行四边形的高度
            C2=Polygon([pt1,pt2,pt3]).area-B2*t2 # 三角形面积
            return [[t1,A1,B1,C1],[t2,-A1,B2-B1,C2-C1]]
        if _type=="vertical":
            pass

    # 获得平移的t值，sign和计算方向相关
    def getT(self,pt,edge,_type,sign,break_points):
        inter=self.getHoriVerInter(pt,edge,_type)
        if len(inter)==0:
            return
        break_points.append((inter[_type]-pt[_type])*sign)

    '''没有考虑不存在的情况/没有考虑直线垂直和水平情况'''
    # 某一点水平或垂直平移后与某直线的交点及其比例
    def getHoriVerInter(self,pt,edge,_type):
        upper_pt=edge[1]
        lower_pt=edge[0]
        if edge[0][1-_type]>edge[1][1-_type]:
            upper_pt=edge[0]
            lower_pt=edge[1]
        if pt[1-_type] in Interval(lower_pt[1-_type], upper_pt[1-_type]):
            # 中间的位置比例
            mid=(upper_pt[1-_type]-pt[1-_type])/(upper_pt[1-_type]-lower_pt[1-_type])
            # mid=(upper_pt[_type]-pt[_type])/(upper_pt[_type]-lower_pt[_type])
            # 水平_type=0，计算的也是x即0
            inter=[0,0]
            inter[_type]=upper_pt[_type]-(upper_pt[_type]-lower_pt[_type])*mid
            inter[1-_type]=pt[1-_type]
            return inter
        return []

    # 旋转后的近邻位置
    def rotationNeighbor(self,poly):
        pass
    
    # 获得Positive和Negative的Edges
    def updateEdgesPN(self):
        # 其他形状的边的情况
        self.horizontal_positive=[]
        self.horizontal_negative=[]
        self.vertical_positive=[]
        self.vertical_negative=[]
        for index,item in enumerate(self.polyList):
            if index!=self.max_miu_index:
                self.appendEdges(self.horizontal_positive,item["horizontal"]["positive"])
                self.appendEdges(self.horizontal_negative,item["horizontal"]["negative"])
                self.appendEdges(self.vertical_positive,item["vertical"]["positive"])
                self.appendEdges(self.vertical_negative,item["vertical"]["negative"])
        # 平移对象的边的情况
        self.target_horizontal_positive=[]
        self.target_horizontal_negative=[]
        self.target_vertical_positive=[]
        self.target_vertical_negative=[]
        self.appendEdges(self.target_horizontal_positive,self.polyList[self.max_miu_index]["horizontal"]["positive"])
        self.appendEdges(self.target_horizontal_negative,self.polyList[self.max_miu_index]["horizontal"]["negative"])
        self.appendEdges(self.target_vertical_positive,self.polyList[self.max_miu_index]["vertical"]["positive"])
        self.appendEdges(self.target_vertical_negative,self.polyList[self.max_miu_index]["vertical"]["negative"])
    
    def appendEdges(self,target,source):
        for edge in source:
            target.append(edge)

    # 寻找最佳位置
    def bestNeighbor(self,poly):
        print("bestNeighbor")
        res=False
        self.updateEdgesPN()
        # 水平移动效果slideNeighbor
        if self.slideNeighbor(poly,"horizontal")==True:
            res=True
        # 垂直移动
        if self.slideNeighbor(poly,"vertical")==True:
            res=True
        # 旋转
        if self.rotationNeighbor(poly)==True:
            res=True

        return res
    
    # 论文 Algorithm1 防止局部最优
    def guidedLocalSearch(self):
        self.phi = [[0]*len(self.polys) for i in range(len(self.cur_polys))] # 惩罚函数
        self.miu_pair=[[0]*len(self.cur_polys) for i in range(len(self.cur_polys))] # 调整后的重叠情况
        self.miu_each=[0 for i in range(len(self.cur_polys))] # 调整后的重叠情况
        self.updateOverlap() # 首先更新重叠
        while self.overlap==True:
            while self.bestNeighbor(self.polys[self.max_miu_index])==True:
                break # 暂时先停止
            self.updateOverlap() # 更新miu
            break

    # 获得当前所有的边的情况
    def updatePolyList(self):
        self.polyList=[]
        for i,poly in enumerate(self.polys):
            edges=GeoFunc.getPolyEdges(poly)
            poly_item={
                "index":i,
                "pts":poly,
                "edges":edges,
                "horizontal":{
                    "positive":[],
                    "negative":[],
                    "neutral":[]
                },
                "vertical":{
                    "positive":[],
                    "negative":[],
                    "neutral":[]
                },
            }
            for edge in edges:
                netural=self.judgeNeutral(poly,edge) # 分别获得水平和垂直的计算结果
                for i,cur in enumerate(["horizontal","vertical"]):
                    if netural[i]==1:
                        poly_item[cur]["positive"].append([edge[0],edge[1]])
                    elif netural[i]==-1:
                        poly_item[cur]["negative"].append([edge[0],edge[1]])
                    else:
                        poly_item[cur]["neutral"].append([edge[0],edge[1]])
            self.polyList.append(poly_item)
    
    # 判断是否
    def judgeNeutral(self,poly,edge):
        e=0.000001
        P=Polygon(poly)
        mid=[(edge[0][0]+edge[1][0])/2,(edge[0][1]+edge[1][1])/2]
        positive_contain=[P.contains(Point([mid[0]+e,mid[1]])),P.contains(Point([mid[0],mid[1]+e]))] # 水平移动/垂直移动
        neutral=[1,1] # 水平移动/垂直移动
        for i,contain in enumerate(positive_contain):
            if abs(edge[0][1-i]-edge[1][1-i])<precision_error:
                neutral[i]=0
            elif positive_contain[0]==True:
                neutral[i]=1
            else:
                neutral[i]=-1
        return neutral
    
class ILSQN():
    '''
    参考资料：2009 An iterated local search algorithm based on nonlinear programming for the irregular strip packing problem
    '''
    def __init__(self,polys):
        self.polys=polys
        

    def MinimizeOverlap(self, oris, v, o):
        '''
        oris: 允许旋转的角度集合
        v: 多边形位置 实际已通过self.polygons得到
        o: 旋转的角度 后期可考虑把多边形封装成类
        '''
        n_polys = self.n_polys
        it = 0
        fitness = 999999
        while it < self.n_mo:
            Q = np.random.permutation(range(n_polys))
            for i in range(n_polys):
                curPoly = self.polygons[Q[i]]
                # 记录原始位置
                top_index = GeoFunc.checkTop(curPoly)
                top = list(curPoly[top_index])
                F = self.evaluate(Q[i])  # 以后考虑旋转
                print('F of',Q[i],':',F)
                v_i = self.CuckooSearch(Q[i])
                self.evaluate(Q[i], v_i)
                F_new = v_i.getF()
                print('new F of',Q[i],':',F)
                if F_new < F:
                    print('polygon', Q[i], v_i.getXY())
                else:
                    # 平移回原位置
                    GeoFunc.slideToPoint(curPoly, curPoly[top_index], top)
            fitness_new = self.evaluateAll()
            if fitness_new == 0:
                return it  # 可行解
            elif fitness_new < fitness:
                fitness = fitness_new
                it = 0
            self.updatePenalty()
            it = it+1
        return it

    def FindBestPosition(self):
        pass

    def SwapTwoPolygons(self):
        pass


if __name__ == "__main__":
    FNS=FNS(getData())
