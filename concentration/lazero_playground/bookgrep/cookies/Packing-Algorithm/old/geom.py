'''
1. 判断包络、凹凸、利用率的函数
2. 获得dominate Point的函数
3. best fit position的函数
'''
import numpy as np
import math
from shapely.geometry import Polygon,Point,mapping,LineString
from shapely.wkt import loads as load_wkt
from shapely.ops import unary_union

# 多边形包络与凹凸的计算
class polyJudge(object):
    def computeEnvelope(self):
        '''
        计算包络凸多边性
        '''
        # 初始化包络形状
        len_envelope=len(self.envelope_polygon)

        # 延长01两个点辅助计算
        polygon_extend=self.envelope_polygon
        polygon_extend.append(self.envelope_polygon[0])
        polygon_extend.append(self.envelope_polygon[1])

        print("————————————————包络计算————————————————")
        i=0
        delete_point=False
        envelope=[]
        print("len_envelope:",len_envelope)
        while i<len_envelope:
            if self.judgeConvex(polygon_extend[i:i+3]):
                envelope.append(polygon_extend[i+1])
                i=i+1
            else:
                envelope.append(polygon_extend[i+2])
                delete_point=True
                i=i+2
        
        self.envelope_polygon=envelope
        
        # 如果有删除结点，就再计算一次
        if delete_point==True:
            self.computeEnvelope()
        
    def polyConvex(self):
        '''
        多边形的凹凸判断
        '''
        poly=self.polygon_vertexs
        poly_extend=poly+poly
        convex=True
        for i in range(len(poly)):
            if self.judgeConvex([poly_extend[i],poly_extend[i+1],poly_extend[i+2]])==False:
                convex=False
                break
        print("convex:",convex)
        return convex


    def judgeConvex(self,points):
        '''
        计算凹凸性
        '''
        # 计算三个判断向量
        AB=[points[1][0]-points[0][0],points[1][1]-points[0][1]]
        CB=[points[1][0]-points[2][0],points[1][1]-points[2][1]]
        OB=[points[1][0]-self.centroid_x,points[1][1]-self.centroid_y]

        # 计算向量的和
        B_B=[AB[0]+CB[0],AB[1]+CB[1]]

        # 计算内积
        multi=B_B[0]*OB[0]+B_B[1]*OB[1]

        # 初始化凹凸判断，并进行基础判断
        convex=False
        if multi>0:
            convex=True

        intersectant=True

        # 通过三个交点情况判断交点是否在外部
        if self.centroid_in==False:
            intersectant0=self.linePoly([points[0],[self.centroid_x,self.centroid_y]])
            intersectant1=self.linePoly([points[1],[self.centroid_x,self.centroid_y]])
            intersectant2=self.linePoly([points[2],[self.centroid_x,self.centroid_y]])
            # 如果三个点和质心都没有交点，绝大部分正常的图形都是需要相反计算
            if intersectant0==None and intersectant1==None and intersectant2==None:
                intersectant=False
                
        if intersectant==True:
            print("判断结果：",convex)
            return convex
        else:
            print("判断结果：",not convex)
            return not convex

    def computeUtilization(self):
        '''
        通过凸多边形计算利用率
        '''
        area=self.polygon.area
        convex_polygon=Polygon(self.envelope_polygon)
        convex_area=convex_polygon.area
        self.utilization=area/convex_area
        print("利用率计算结果：",self.utilization)

    def arrInverse(self,_arr):
        _new=[]
        _len=len(_arr)
        for i in range(_len):
            _new.append(_arr[_len-i-1])
        return _new

class getDP(object):
    '''
    获得 Dominate Point
    参考：https://www.sciencedirect.com/science/article/pii/S0377221713005080
    '''
    def __init__(self,NFP,pp):
        self.NFP=NFP

    # 三个函数通过NFP获得DOminate Point
    def getDP(self,pp):

        NFP_extend=self.NFP+self.NFP
        EP=pp.envelope_polygon+pp.envelope_polygon[:1]
        i=0
        j=0
        begin=False
        points_max=[]
        while i<len(EP)-2:
            line=LineString([EP[i],EP[i+1]])
            points=[]
            while True:
                if begin==False:
                    if NFP_extend[j]==EP[i]:
                        begin=True
                        j=j+1
                    else:
                        j=j+1
                        continue
                if begin==True:
                    if NFP_extend[j]!=EP[i+1]:
                        points.append(Point(NFP_extend[j]))
                        j=j+1
                    else:
                        begin=False
                        break
            if len(points)>0:
                points_max.append(self.getFar(points,line))
            i=i+1

        if len(points_max)>0:
            DP=self.getMax(points_max)
            return DP
        else:
            return False

    def getMax(self,points):
        '''
        获得最大的值，可能出现多个点
        '''
        _max=points[0]
        for i in range(1,len(points)):
            if points[i]["distance"]>_max["distance"]:
                _max=points[i]
        return _max

    def getFar(self,points,line):
        '''
        获得离距离最远的，可能出现多个点
        '''
        _max={
            "cord":[0,0],
            "distance":0
        }
        for point in points:
            pt_dis=point.distance(line)
            if pt_dis>_max["distance"]:
                _max["distance"]=pt_dis
                cord=mapping(point)["coordinates"]
                _max["cord"]=[cord[0],cord[1]]
        return _max