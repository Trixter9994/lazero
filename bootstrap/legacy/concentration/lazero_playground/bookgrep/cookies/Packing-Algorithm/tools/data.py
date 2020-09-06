import pandas as pd # 读csv
import csv # 写csv
import numpy as np # 数据处理
import os
import re
import json
import matplotlib.pyplot as plt
import time
import random
import math
from polygon import PltFunc,GeoFunc,NFP
from shapely.geometry import Polygon,mapping
from vectorization import vectorFunc

# Preprocess train data
class trainDataProcess(object):
    def __init__(self):
        self.combinateTestData()

    def processAllFiles(self):
        '''
        读取全部的数据，并选择合适的项目加入训练/测试集
        '''
        filePath="/Users/sean/Documents/Projects/Packing-Algorithm/record/synthetic/"
        all_files=[]

        for i,j,k in os.walk(filePath):
            files=k
        aim_files=[]

        for _file in files:
            if _file!="readme.md" and _file!=".DS_Store":
                aim_files.append(_file)

    # 两个形状的情况下
    def combinateFiles(self):
        # convex = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/record/convex.csv")
        # for i in range(0,success.shape[0]):
        for i in range(0,1):
            index=success["index1"][i]
            with open("/Users/sean/Documents/Projects/Data/Shapes/pre_train.csv","a+") as csvfile:
                writer = csv.writer(csvfile)
                _time=success["time"][i]
                index1=success["index1"][i]
                index2=success["index2"][i]
                vertices_num1=success["vertices_num1"][i]
                vertices_num2=success["vertices_num2"][i]
                fitness=success["fitness"][i]
                relative_position=success["relative_position"][i]
                poly1=success["final_poly1"][i]
                poly2=success["final_poly2"][i]
                writer.writerows([[i,_time,index1,index2,vertices_num1,vertices_num2,fitness,relative_position,poly1,poly2,convex["vec_8"][index1],convex["vec_12"][index1],convex["vec_16"][index1],convex["vec_24"][index1],convex["vec_32"][index1],convex["vec_8"][index2],convex["vec_12"][index2],convex["vec_16"][index2],convex["vec_24"][index2],convex["vec_32"][index2]]])

    def combinateVecConvex(self):
        result = pd.read_csv("/Users/sean/Documents/Projects/Data/result.csv")
        convex = pd.read_csv("/Users/sean/Documents/Projects/Data/convex_vec.csv")
        for i in range(0,convex.shape[0]):
        # for i in range(0,1):
            index=[result["num1"][i],result["num2"][i],result["num3"][i],result["num4"][i]]
            # 获得几个x
            x_8=self.normVec(json.loads(convex["vec_8"][index[0]])+json.loads(convex["vec_8"][index[1]])+json.loads(convex["vec_8"][index[2]])+json.loads(convex["vec_8"][index[3]]))
            x_16=self.normVec(json.loads(convex["vec_16"][index[0]])+json.loads(convex["vec_16"][index[1]])+json.loads(convex["vec_16"][index[2]])+json.loads(convex["vec_16"][index[3]]))
            x_32=self.normVec(json.loads(convex["vec_32"][index[0]])+json.loads(convex["vec_32"][index[1]])+json.loads(convex["vec_32"][index[2]])+json.loads(convex["vec_32"][index[3]]))
            x_64=self.normVec(json.loads(convex["vec_64"][index[0]])+json.loads(convex["vec_64"][index[1]])+json.loads(convex["vec_64"][index[2]])+json.loads(convex["vec_64"][index[3]]))
            x_128=self.normVec(json.loads(convex["vec_128"][index[0]])+json.loads(convex["vec_128"][index[1]])+json.loads(convex["vec_128"][index[2]])+json.loads(convex["vec_128"][index[3]]))
            x_256=self.normVec(json.loads(convex["vec_256"][index[0]])+json.loads(convex["vec_256"][index[1]])+json.loads(convex["vec_256"][index[2]])+json.loads(convex["vec_256"][index[3]]))
            # 获得四个形状
            poly1=json.loads(result["poly1"][i])
            poly2=json.loads(result["poly2"][i])
            poly3=json.loads(result["poly3"][i])
            poly4=json.loads(result["poly4"][i])
            # 获得几个中心计算出y的值
            y=self.normPosi(getPt(Polygon(poly1).centroid)+getPt(Polygon(poly2).centroid)+getPt(Polygon(poly3).centroid)+getPt(Polygon(poly4).centroid))
            print(y)
            with open("/Users/sean/Documents/Projects/Data/train.csv","a+") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows([[i,time.asctime(time.localtime(time.time())),index[0],index[1],index[2],index[3],poly1,poly2,poly3,poly4,x_8,x_16,x_32,x_64,x_128,x_256,y]])

    def combinateTestData(self):
        shapes = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/euro_data/train_test/blaz_vec.csv")
        for i in range(0,60):
            index=[random.randint(0,6),random.randint(0,6),random.randint(0,6),random.randint(0,6)]
            shape1=json.loads(shapes["poly"][index[0]])
            shape2=json.loads(shapes["poly"][index[1]])
            shape3=json.loads(shapes["poly"][index[2]])
            shape4=json.loads(shapes["poly"][index[3]])
            GeoFunc.normData(shape1,150)
            GeoFunc.normData(shape2,150)
            GeoFunc.normData(shape3,150)
            GeoFunc.normData(shape4,150)
            with open("/Users/sean/Documents/Projects/Packing-Algorithm/euro_data/train_test/blaz_trian_test.csv","a+") as csvfile:
                writer = csv.writer(csvfile)
                x_8=self.normVec(json.loads(shapes["vec_8"][index[0]])+json.loads(shapes["vec_8"][index[1]])+json.loads(shapes["vec_8"][index[2]])+json.loads(shapes["vec_8"][index[3]]))
                x_16=self.normVec(json.loads(shapes["vec_16"][index[0]])+json.loads(shapes["vec_16"][index[1]])+json.loads(shapes["vec_16"][index[2]])+json.loads(shapes["vec_16"][index[3]]))
                x_32=self.normVec(json.loads(shapes["vec_32"][index[0]])+json.loads(shapes["vec_32"][index[1]])+json.loads(shapes["vec_32"][index[2]])+json.loads(shapes["vec_32"][index[3]]))
                x_64=self.normVec(json.loads(shapes["vec_64"][index[0]])+json.loads(shapes["vec_64"][index[1]])+json.loads(shapes["vec_64"][index[2]])+json.loads(shapes["vec_64"][index[3]]))
                x_128=self.normVec(json.loads(shapes["vec_128"][index[0]])+json.loads(shapes["vec_128"][index[1]])+json.loads(shapes["vec_128"][index[2]])+json.loads(shapes["vec_128"][index[3]]))
                x_256=self.normVec(json.loads(shapes["vec_256"][index[0]])+json.loads(shapes["vec_256"][index[1]])+json.loads(shapes["vec_256"][index[2]])+json.loads(shapes["vec_256"][index[3]]))
                writer.writerows([[i,time.asctime(time.localtime(time.time())),index[0],index[1],index[2],index[3],shape1,shape2,shape3,shape4,x_8,x_16,x_32,x_64,x_128,x_256]])


    def normTrain(self):
        pre_train = pd.read_csv("/Users/sean/Documents/Projects/Data/pre_train.csv")
        for i in range(0,pre_train):
            # with open("/Users/sean/Documents/Projects/Data/Shapes/train.csv","a+") as csvfile:
            with open("/Users/sean/Documents/Projects/Data/Shapes/train.csv","a+") as csvfile:
                writer = csv.writer(csvfile)
                x_8=self.normVec(json.loads(pre_train["vec1_8"][i])+json.loads(pre_train["vec2_8"][i]))
                x_12=self.normVec(json.loads(pre_train["vec1_12"][i])+json.loads(pre_train["vec2_12"][i]))
                x_16=self.normVec(json.loads(pre_train["vec1_16"][i])+json.loads(pre_train["vec2_16"][i]))
                x_24=self.normVec(json.loads(pre_train["vec1_24"][i])+json.loads(pre_train["vec2_24"][i]))
                x_32=self.normVec(json.loads(pre_train["vec1_32"][i])+json.loads(pre_train["vec2_32"][i]))
                y=self.normPosi(json.loads(pre_train["relative_position"][i]))
                writer.writerows([[i,x_8,x_12,x_16,x_24,x_32,y]])
            
    def normVec(self,_arr):
        '''
        向量化结果全部归化到[-1,1]
        '''
        new_arr=[]
        for item in _arr:
            if item==9999999:
                new_arr.append(0)
            else:
                new_arr.append(item/150) # 全部正数
                # new_arr.append((item+2000)/4000)
        return new_arr
    
    def judgePosi(self,_arr):
        '''
        判断向量化的值全为正值/有负值，部分Vectorization后的特征值可能会小于0
        '''
        positive=True
        for item in _arr:
            if item<0:
                positive=False
                break
        return positive
    
    def normPosi(self,_arr):
        '''
        所有位置标准化到[0,1]
        '''
        new_arr=[]
        for item in _arr:
            new_arr.append(item/2400)
        return new_arr

def computeVec():
    df = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/euro_data/blaz1.csv")
    # df = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/record/convex.csv")
    for i in range(0,df.shape[0]):
        poly=json.loads(df['polygon'][i])
        res=[]
        for num in [8,16,32,64,128,256]:
            vf=vectorFunc(poly,cut_nums=num)
            res.append(vf.vector)
        with open("/Users/sean/Documents/Projects/Packing-Algorithm/euro_data/blaz_vec.csv","a+") as csvfile: 
        # with open("/Users/sean/Documents/Projects/Packing-Algorithm/euro_data/blaz_vec.csv","a+") as csvfile: 
            writer = csv.writer(csvfile)
            # 写入index,time,angle,vertices,polygon
            # writer.writerows([[i,time.asctime(time.localtime(time.time())),df['angle'][i],df['vertices'][i],df['polygon'][i],res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7]]])
            writer.writerows([[i,time.asctime(time.localtime(time.time())),df['polygon'][i],res[0],res[1],res[2],res[3],res[4],res[5]]])

# Generate arbitrary shapes. 
class getShape(object):
    def getConvexRandom():
        polygon=[]
        num=10
        for i in range(0,num):
            # radian=(2/num)*math.pi*i+math.pi*random.randrange(0,5,1)/12 # convex 4的角度
            radian=(2/num)*math.pi*i+math.pi*random.randrange(0,3,1)/(num*2) # convex num>4的角度
            radius=random.randrange(200,500,100)
            pt=[radius*math.cos(radian),radius*math.sin(radian)]
            polygon.append(pt)
        GeoFunc.slidePoly(polygon,750,750)
        storePolygon(polygon,num=num)
        PltFunc.addPolygon(polygon)
        PltFunc.showPlt()
    
def testData():
    df = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/record/convex.csv")
    poly1=json.loads(df['polygon'][4674])
    poly2=json.loads(df['polygon'][3652])
    nfp=NFP(poly1,poly2) # NFP计算，error<0表示错误
    PltFunc.addPolygon(poly1)
    PltFunc.addPolygon(poly2)
    # PltFunc.addPolygonColor(nfp.nfp)
    # PltFunc.showPlt()
    bfp=bestFitPosition(nfp,False)

def getPt(point):
    mapping_result=mapping(point)
    return [mapping_result["coordinates"][0],mapping_result["coordinates"][1]]

# 存储生成的形
def storePolygon(poly,**kw):
    if len(kw)>0:
        with open("/Users/sean/Documents/Projects/Packing-Algorithm/record/synthetic/convex_"+str(kw["num"])+".csv","a+") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[time.asctime(time.localtime(time.time())),0,poly]])
    else:
        with open("/Users/sean/Documents/Projects/Packing-Algorithm/record/synthetic/convex.csv","a+") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[time.asctime(time.localtime(time.time())),poly]])

def cleanFail():
    df = pd.read_csv("/Users/sean/Documents/Projects/Data/Shapes/fail_part.csv")
    for i in range(0,2000):
        print("第",i,"个计算")
        poly1=json.loads(df['poly1'][i])
        poly2=json.loads(df['poly2'][i])
        nfp=NFP(poly1,poly2) # NFP计算，error<0表示错误
        if nfp.error<1:
            with open("/Users/sean/Documents/Projects/Data/Shapes/now_fail.csv","a+") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows([[i,poly1,poly2]])            
    

# 读取历史的排样结果
def readRecord():
    line=122
    df = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/arrangements/record.csv")
    polygons=json.loads(df["result"][line])
    for poly in polygons:
        PltFunc.addPolygon(poly)
    PltFunc.showPlt()

def readPoly():
    line=1000*10+random.randint(0,1000)
    df = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/record/convex.csv")
    polygon=json.loads(df["polygon"][line])
    PltFunc.addPolygon(polygon)
    PltFunc.showPlt()


ef getPolyArray(polyList):
    poly_array=[]
    for item in polyList:
        poly_array.append(item["poly"])
    return poly_array

def getConvex():
    df = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/record/convex.csv")
    polyList=[]
    poly_index=[random.randint(0,11200),random.randint(0,11200),random.randint(0,11200),random.randint(0,11200)]

    for i in poly_index:
        polyList.append({
            "poly":json.loads(df['polygon'][i]),
            "num":i
        })
    
    return getAllSequence(polyList),polyList

# 四个形状一共24个组合
def getAllSequence(polyList):
    sequenceList=[]
    sequenceList.append([polyList[0],polyList[1],polyList[2],polyList[3]])
    sequenceList.append([polyList[0],polyList[1],polyList[3],polyList[2]])
    sequenceList.append([polyList[0],polyList[2],polyList[1],polyList[3]])
    sequenceList.append([polyList[0],polyList[2],polyList[3],polyList[1]])
    sequenceList.append([polyList[0],polyList[3],polyList[2],polyList[1]])
    sequenceList.append([polyList[0],polyList[3],polyList[1],polyList[2]])

    sequenceList.append([polyList[1],polyList[0],polyList[2],polyList[3]])
    sequenceList.append([polyList[1],polyList[0],polyList[3],polyList[2]])
    sequenceList.append([polyList[1],polyList[2],polyList[0],polyList[3]])
    sequenceList.append([polyList[1],polyList[2],polyList[3],polyList[0]])
    sequenceList.append([polyList[1],polyList[3],polyList[0],polyList[2]])
    sequenceList.append([polyList[1],polyList[3],polyList[2],polyList[0]])

    sequenceList.append([polyList[2],polyList[0],polyList[1],polyList[3]])
    sequenceList.append([polyList[2],polyList[0],polyList[3],polyList[1]])
    sequenceList.append([polyList[2],polyList[1],polyList[0],polyList[3]])
    sequenceList.append([polyList[2],polyList[1],polyList[3],polyList[0]])
    sequenceList.append([polyList[2],polyList[3],polyList[0],polyList[1]])
    sequenceList.append([polyList[2],polyList[3],polyList[1],polyList[0]])

    sequenceList.append([polyList[3],polyList[0],polyList[1],polyList[2]])
    sequenceList.append([polyList[3],polyList[0],polyList[2],polyList[1]])
    sequenceList.append([polyList[3],polyList[1],polyList[0],polyList[2]])
    sequenceList.append([polyList[3],polyList[1],polyList[2],polyList[0]])
    sequenceList.append([polyList[3],polyList[2],polyList[0],polyList[1]])
    sequenceList.append([polyList[3],polyList[2],polyList[1],polyList[0]])

    return sequenceList

def getOneSequence():
    sequenceList,polyList=getConvex()
    min_height=9999999999
    min_sequence=[]
    for i,sequence in enumerate(sequenceList):
        print("第",i,"个组合")
        polygons=getPolyArray(sequence)
        pp=PlacePolygons(polygons)
        if pp.contain_height<min_height:
            min_height=pp.contain_height
            min_sequence=sequence
    print("最终高度:",min_height)
    print("最终序列:",min_sequence)
    return min_height,min_sequence

if __name__ == '__main__':
    # bf=bestFit()
    # tdp=trainDataProcess()
    # bs=buildShape()
    # cb=combinateFile()
    # tr=trainResult()
    # for i in range(0,1200):
        # getShape.getConvexRandom()

    # buildData()
    # testData()
    # for i in range(0,20):
        # readPoly()
    trainDataProcess()
    # computeVec()
    # buildTest()
    # cleanFail()

    # 获得足够的形状组合
    for i in range(0,10000):
        print("#################计算第",i+1,"个序列#################")
        height,sequence=getOneSequence()
        with open("/Users/sean/Documents/Projects/Data/result.csv","a+") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([[time.asctime(time.localtime(time.time())),height,sequence[0]["num"],sequence[1]["num"],sequence[2]["num"],sequence[3]["num"],sequence[0]["poly"],sequence[1]["poly"],sequence[2]["poly"],sequence[3]["poly"]]])
