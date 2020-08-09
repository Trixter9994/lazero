# 参考资料 Evolution of a salesman: A complete genetic algorithm tutorial for Python
# https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
import numpy as np, random, operator, pandas as pd, matplotlib.pyplot as plt
from polygon import GeoFunc,NFP,PltFunc,RatotionPoly
import json
from shapely.geometry import Polygon,mapping
from shapely import affinity
import csv
import time
import multiprocessing
import datetime
cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(processes=cores)

class BottomLeftFill(object):
    def __init__(self,width,polygons):
        self.choose_nfp=False
        self.width=width
        self.height=150000
        self.polygons=polygons
        # self.storeOrginal()
        # print(polygons)
        self.placeFirstPoly()

        # print("共",len(polygons),"个形状")
        for i in range(1,len(polygons)):
            print("##############################放置第",i+1,"个形状#################################")
            self.placePoly(i)
        
        self.getHeight()
        print("height:",self.contain_height)
        
        # self.showAll()
        self.storeResult()

    def storeOrginal(self):
        with open("/Users/sean/Documents/Projects/Packing-Algorithm/arrangements/orginal.csv","a+") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[time.asctime(time.localtime(time.time())),"blaze",self.polygons]])

    def storeResult(self):
        with open("/Users/sean/Documents/Projects/Packing-Algorithm/record/record.csv","a+") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[time.asctime(time.localtime(time.time())),"blaze",self.contain_height,self.polygons]])

    def getHeight(self):
        _max=0
        for i in range(1,len(self.polygons)):
            top_index=GeoFunc.checkTop(self.polygons[i])
            top=self.polygons[i][top_index][1]
            if top>_max:
                _max=top
        self.contain_height=_max
        PltFunc.addLine([[0,self.contain_height],[self.width,self.contain_height]],color="blue")
    
    def getMinTop(self,polygons):
        min_top=9999999999
        for poly in polygons:
            bt_index=GeoFunc.checkTop(poly)
            if poly[bt_index][1]<min_top:
                min_top=poly[bt_index][1]
        return min_top

    def placePoly(self,index):
        '''
        放置某一个index的形状进去
        '''
        adjoin=self.polygons[index]
        ifp=self.getInnerFitRectangle(self.polygons[index])
        differ_region=Polygon(ifp)
        multi=True
        if multi==True:
            if self.choose_nfp==True and index>8:
                target_polygon=self.polygons[index-8:index]
                bottom_height=self.getMinTop(target_polygon)+300
                differ_region=differ_region.difference(Polygon([[0,0],[self.width,0],[self.width,bottom_height],[0,bottom_height]]))
            else:
                target_polygon=self.polygons[0:index]
            tasks=[(main,adjoin) for main in target_polygon]
            res=pool.starmap(NFP,tasks)
            for item in res:
                nfp=item.nfp
                differ_region=differ_region.difference(Polygon(nfp))
        else:
            for main_index in range(0,index):
                main=self.polygons[main_index]
                nfp=NFP(main,adjoin).nfp
                differ_region=differ_region.difference(Polygon(nfp))

        # print(differ_region)
        differ=GeoFunc.polyToArr(differ_region)

        differ_index=self.getBottomLeft(differ)
        refer_pt_index=GeoFunc.checkTop(adjoin)
        GeoFunc.slideToPoint(self.polygons[index],adjoin[refer_pt_index],differ[differ_index])        

    def getBottomLeft(self,poly):
        bl=[] # bottom left的全部点
        min_y=999999
        # 采用重心最低的原则
        for i,pt in enumerate(poly):
            pt_object={
                    "index":i,
                    "x":pt[0],
                    "y":pt[1]
            }
            if pt[1]<min_y:
                # 如果y更小，那就更新bl
                min_y=pt[1]
                bl=[pt_object]
            elif pt[1]==min_y:
                # 相同则添加这个点
                bl.append(pt_object)
            else:
                pass
        if len(bl)==1:
            return bl[0]["index"]
        else:
            min_x=bl[0]["x"]
            one_pt=bl[0]
            for pt_index in range(1,len(bl)):
                if bl[pt_index]["x"]<min_x:
                    one_pt=bl[pt_index]
                    min_x=one_pt["x"]
            return one_pt["index"]

    '''修改展示高度'''
    def showAll(self):
        for i in range(0,len(self.polygons)):
            PltFunc.addPolygon(self.polygons[i])
        length=max(self.width,self.contain_height)
        PltFunc.addLine([[self.width,0],[self.width,self.contain_height]],color="blue")
        PltFunc.showPlt(width=length,height=length)
    
    def placeFirstPoly(self):
        '''
        放置第一个形状进去，并平移到left-bottom
        '''
        poly=self.polygons[0]
        poly_index=GeoFunc.checkTop(poly)
        left_index,bottom_index,right_index,top_index=GeoFunc.checkBound(poly)
        
        move_x=poly[left_index][0]
        move_y=poly[bottom_index][1]
        GeoFunc.slidePoly(poly,0,-move_y)

    def getInnerFitRectangle(self,poly):
        '''
        获得IFR，同时平移到left-bottom
        '''
        poly_index=GeoFunc.checkTop(poly)
        left_index,bottom_index,right_index,top_index=GeoFunc.checkBound(poly)
        
        move_x=poly[left_index][0]
        move_y=poly[bottom_index][1]
        GeoFunc.slidePoly(poly,-move_x,-move_y)

        refer_pt=[poly[poly_index][0],poly[poly_index][1]]
        width=self.width-poly[right_index][0]
        height=self.height-poly[top_index][1]

        IFR=[refer_pt,[refer_pt[0]+width,refer_pt[1]],[refer_pt[0]+width,refer_pt[1]+height],[refer_pt[0],refer_pt[1]+height]]
        
        return IFR
    
    def getInnerFitRectangleNew(self,poly):
        '''
        获得IFR，不平移
        '''
        poly_index=GeoFunc.checkBottom(poly)
        left_index,bottom_index,right_index,top_index=GeoFunc.checkBound(poly)
        
        move_x=poly[left_index][0]
        move_y=poly[top_index][1]
        new_poly=GeoFunc.getSlide(poly,-move_x,-move_y)

        refer_pt=[new_poly[poly_index][0],new_poly[poly_index][1]]
        width=self.width-new_poly[right_index][0]
        height=self.height-new_poly[bottom_index][1]

        IFR=[refer_pt,[refer_pt[0]+width,refer_pt[1]],[refer_pt[0]+width,refer_pt[1]+height],[refer_pt[0],refer_pt[1]+height]]
        print("计算出结果:",IFR)

        return IFR
    
    # 形状收缩
    def normData(self,num):
        for poly in self.polygons:
            for ver in poly:
                ver[0]=ver[0]*num
                ver[1]=ver[1]*num

class DJD(object):
    def __init__(self):
        pass

class SA(object):
    '''
    '''
    def coordinate_init(size):
        #产生坐标字典
        coordinate_dict = {}
        coordinate_dict[0] = (0, 0)#起点是（0，0）
        for i in range(1, size + 1):#顺序标号随机坐标
            coordinate_dict[i] = (np.random.uniform(0, size), np.random.uniform(0, size))
        coordinate_dict[size + 1] = (0, 0)#终点是（0,0)
        return coordinate_dict
 
    def distance_matrix(coordinate_dict,size):#生成距离矩阵
        d=np.zeros((size+2,size+2))
        for i in range(size+1):
            for j in range(size+1):
                if(i==j):
                    continue
                if(d[i][j]!=0):
                    continue
                x1 = coordinate_dict[i][0]
                y1 = coordinate_dict[i][1]
                x2 = coordinate_dict[j][0]
                y2 = coordinate_dict[j][1]
                distance=np.sqrt((x1-x2)**2+(y1-y2)**2)
                if(i==0):
                    d[i][j]=d[size+1][j]=d[j][i]=d[j][size+1]=distance
                else:
                    d[i][j]=d[j][i]=distance
        return d
 
    def path_length(d_matrix,path_list,size):#计算路径长度
        length=0
        for i in range(size+1):
            length+=d_matrix[path_list[i]][path_list[i+1]]
        return length
 
    def new_path(path_list,size):
        #二交换法
        change_head = np.random.randint(1,size+1)
        change_tail = np.random.randint(1,size+1)
        if(change_head>change_tail):
            change_head,change_tail=change_tail,change_head
        change_list = path_list[change_head:change_tail + 1]
        change_list.reverse()#change_head与change_tail之间的路径反序
        new_path_list = path_list[:change_head] + change_list + path_list[change_tail + 1:]
        return change_head,change_tail,new_path_list
 
    def diff_old_new(d_matrix,path_list,new_path_list,head,tail):#计算新旧路径的长度之差
        old_length=d_matrix[path_list[head-1]][path_list[head]]+d_matrix[path_list[tail]][path_list[tail+1]]
        new_length=d_matrix[new_path_list[head-1]][new_path_list[head]]+d_matrix[new_path_list[tail]][new_path_list[tail+1]]
        delta_p=new_length-old_length
        return delta_p
 
    def run(self):
        T_start=2000#起始温度
        T_end=1e-20#结束温度
        a=0.995#降温速率
        Lk=50#内循环次数,马尔科夫链长
        size=20
        coordinate_dict=coordinate_init(size)
        print(coordinate_dict)#打印坐标字典
        path_list=list(range(size+2))#初始化路径
        d=distance_matrix(coordinate_dict,size)#距离矩阵的生成
        best_path=path_length(d,path_list,size)#初始化最好路径长度
        print('初始路径:',path_list)
        print('初始路径长度:',best_path)
        best_path_temp=[]#记录每个温度下最好路径长度
        best_path_list=[]#用于记录历史上最好路径
        balanced_path_list=path_list#记录每个温度下的平衡路径
        balenced_path_temp=[]#记录每个温度下平衡路径(局部最优)的长度
        while T_start>T_end:
            for i in range(Lk):
                head, tail, new_path_list = new_path(path_list, size)
                delta_p = diff_old_new(d, path_list, new_path_list, head, tail)
                if delta_p < 0:#接受状态
                    balanced_path_list=path_list = new_path_list
                    new_len=path_length(d,path_list,size)
                    if(new_len<best_path):
                        best_path=new_len
                        best_path_list=path_list
                elif np.random.random() < np.exp(-delta_p / T_start):#以概率接受状态
                    path_list = new_path_list
            path_list=balanced_path_list#继承该温度下的平衡状态（局部最优）
            T_start*=a#退火
            best_path_temp.append(best_path)
            balenced_path_temp.append(path_length(d,balanced_path_list,size))
        print('结束温度的局部最优路径:',balanced_path_list)
        print('结束温度的局部最优路径长度:',path_length(d,balanced_path_list,size))
        print('最好路径:',best_path_list)
        print('最好路径长度:',best_path)
        x=[]
        y=[]
        for point in best_path_list:
            x.append(coordinate_dict[point][0])
            y.append(coordinate_dict[point][1])
    
        plt.figure(1)
        plt.subplot(311)
        plt.plot(balenced_path_temp)#每个温度下平衡路径长度
        plt.subplot(312)
        plt.plot(best_path_temp)#每个温度下最好路径长度
        plt.subplot(313)
        plt.scatter(x,y)
        plt.plot(x,y)#路径图
        plt.grid()
        plt.show()


def getData():
    index=1
    '''报错数据集有（空心）：han,jakobs1,jakobs2 '''
    '''形状过多暂时未处理：shapes、shirt、swim、trousers'''
    name=["ga","albano","blaz1","blaz2","dighe1","dighe2","fu","han","jakobs1","jakobs2","mao","marques","shapes","shirts","swim","trousers","convex"]
    print("开始处理",name[index],"数据集") # ga为测试数据集
    '''暂时没有考虑宽度，全部缩放来表示'''
    scale=[100,0.25,100,100,20,20,20,10,20,20,0.5,20,50,1,1,1,1,1,1,1]
    print("缩放",scale[index],"倍")
    df = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/euro_data/"+name[index]+".csv")
    polygons=[]
    for i in range(0,df.shape[0]):
        for j in range(0,df['num'][i]):
            poly=json.loads(df['polygon'][i])
            GeoFunc.normData(poly,scale[index])
            polygons.append(poly)
    return getDecreasing(polygons)
    # return polygons

def getDecreasing(polygons):
    poly_list=[]
    for poly in polygons:
        poly_list.append([poly,Polygon(poly).area])
    poly_list=sorted(poly_list,key=lambda x:(x[1]),reverse=True)
    new_polygons=[]
    for item in poly_list:
        new_polygons.append(item[0])
    return new_polygons

def getConvex():
    df = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/record/convex.csv")
    polygons=[]
    poly_index=[]
    for i in range(20):
        poly_index.append(random.randint(0,11200))
    # poly_index=[1000,2000,3000,4000,5000,6000,7000]
    # poly_index=[1000,2000,3000]
    poly_index=[5579, 2745, 80, 6098, 3073, 8897, 4871, 4266, 3477, 3266, 8016, 4563, 1028, 10842, 1410, 7254, 5953, 82, 1715, 300]
    for i in poly_index:
        poly=json.loads(df['polygon'][i])
        polygons.append(poly)
    print("序列位置:",poly_index)
    return polygons

if __name__=='__main__':
    starttime = datetime.datetime.now()
    # GA(getConvex())
    bfl=BottomLeftFill(1500,getConvex())
    endtime = datetime.datetime.now()
    print (endtime - starttime)
    bfl.showAll()