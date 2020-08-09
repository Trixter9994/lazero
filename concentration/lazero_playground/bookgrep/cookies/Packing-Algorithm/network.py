'''
   This file is used for train model for two polygons' combination
   Data Url for Type1: https://drive.google.com/open?id=1omrW846HoUXfwZ7UgstbvlVXWqWrdHt2
   Data Url for Type2: https://drive.google.com/open?id=1W1iLYUZGj2j2gKvGiUCBrvrvhuYiawsT
'''
import numpy as np
import json
from keras.models import Sequential
from keras import models
from keras import layers
from keras.models import load_model
from keras import optimizers
import matplotlib.pyplot as plt
import random
import pandas as pd
import time
import csv
from tools.nfp import GeoFunc,PltFunc,NFP,PlacePolygons
from shapely.geometry import Polygon,mapping

class trainModel(object):
   def __init__(self):
      pass
   
   def dataLoad(self):
      '''
      数据加载并处理为np数组
      '''
      x_val,y_val=[],[]
      x_train,y_train=[],[]

      data=pd.read_csv("/Users/sean/Documents/Projects/Data/train.csv")
      for index, row in data.iterrows(): # 遍历行处理
         if index<1300:
                x_train.append(json.loads(row["x_128"]))
                y_train.append(json.loads(row["y"]))
         elif index<2600:
                x_val.append(json.loads(row["x_128"]))
                y_val.append(json.loads(row["y"]))
         else:
            pass
      
      x_val=np.array(x_val)
      y_val=np.array(y_val)

      x_train=np.array(x_train)
      y_train=np.array(y_train)

      self.trainModel(x_val,y_val,x_val,y_val)

   def modelRealTest(self):
      model = load_model("/Users/sean/Documents/Projects/Packing-Algorithm/model/128.h5")
      blaz = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/euro_data/blaz1.csv")
      vec=json.loads(blaz["vec_128"][0])
      

   def testModelFour(self):
      '''
      测试训练结果, 使用未作为训练集的数据进行测试
      '''
      model = load_model("/Users/sean/Documents/Projects/Packing-Algorithm/model/128.h5")
      # train = pd.read_csv("/Users/sean/Documents/Projects/Packing-Algorithm/euro_data/train_test/blaz_trian_test.csv")
      train = pd.read_csv("/Users/sean/Documents/Projects/Data/train.csv")

      # index=random.randint(0,89)
      index=random.randint(1300,2300)
      print(index)

      vec=json.loads(train["x_128"][index])
      poly1=json.loads(train["poly1"][index])
      poly2=json.loads(train["poly2"][index])
      poly3=json.loads(train["poly3"][index])
      poly4=json.loads(train["poly4"][index])
      poly1_pre=json.loads(train["poly1"][index])
      poly2_pre=json.loads(train["poly2"][index])
      poly3_pre=json.loads(train["poly3"][index])
      poly4_pre=json.loads(train["poly4"][index])

      # 根据模型进行预测
      X=np.array([vec])
      yhat = model.predict(X, verbose=0)
      num=2400
      centroid1_pre=[yhat[0][0]*num,yhat[0][1]*num]
      centroid2_pre=[yhat[0][2]*num,yhat[0][3]*num]
      centroid3_pre=[yhat[0][4]*num,yhat[0][5]*num]
      centroid4_pre=[yhat[0][6]*num,yhat[0][7]*num]


      centroid1=self.getPt(Polygon(poly1).centroid)
      centroid2=self.getPt(Polygon(poly2).centroid)
      centroid3=self.getPt(Polygon(poly3).centroid)
      centroid4=self.getPt(Polygon(poly4).centroid)

      GeoFunc.slidePoly(poly1_pre,centroid1_pre[0]-centroid1[0],centroid1_pre[1]-centroid1[1])
      GeoFunc.slidePoly(poly2_pre,centroid2_pre[0]-centroid2[0],centroid2_pre[1]-centroid2[1])
      GeoFunc.slidePoly(poly3_pre,centroid3_pre[0]-centroid3[0],centroid3_pre[1]-centroid3[1])
      GeoFunc.slidePoly(poly4_pre,centroid4_pre[0]-centroid4[0],centroid4_pre[1]-centroid4[1])

      PltFunc.addPolygon(poly1)
      PltFunc.addPolygon(poly2)
      PltFunc.addPolygon(poly3)
      PltFunc.addPolygon(poly4)

      for poly in self.getSequence([poly1_pre,poly2_pre,poly3_pre,poly4_pre]):
         PltFunc.addPolygonColor(poly)
      
      # PltFunc.addPolygonColor(poly1_pre)
      # PltFunc.addPolygonColor(poly2_pre)
      # PltFunc.addPolygonColor(poly3_pre)
      # PltFunc.addPolygonColor(poly4_pre)
      # with open("/Users/sean/Documents/Projects/Packing-Algorithm/record/prediction_four.csv","a+") as csvfile: 
      #    writer = csv.writer(csvfile)
      #    writer.writerows([[index,[poly1,poly2,poly3,poly4],[poly1_pre,poly2_pre,poly3_pre,poly4_pre]]])

      PltFunc.showPlt()
   
   def getSequence(self,polys):
      polyList=[]
      for poly in polys:
         centroid=self.getPt(Polygon(poly).centroid)
         polyList.append({
            "poly":poly,
            "centroid":[centroid[0],centroid[1]],
            "norm":centroid[0]+centroid[1]
         })
      sorted(polyList,key=lambda poly: poly["norm"])
      sequence=[]
      for item in polyList:
         sequence.append(item["poly"])
      pp=PlacePolygons(1000,sequence)   
      return pp.polygons

   def testModelTwo(self):
      '''
      测试训练结果, 使用未作为训练集的数据进行测试
      '''
      model = load_model("/Users/sean/Documents/Projects/Packing-Algorithm/model/test.h5")
      pre_train = pd.read_csv("/Users/sean/Documents/Projects/Data/Shapes/train2.2/pre_train.csv")
      train = pd.read_csv("/Users/sean/Documents/Projects/Data/Shapes/train2.2/train.csv")

      vec=[]
      position=[]
      poly1=[]
      poly2=[]

      index=random.randint(0,10000)
      print(index)
      vec=json.loads(train["x_32"][index])
      poly1=json.loads(pre_train["poly1"][index])
      poly2=json.loads(pre_train["poly2"][index])
      position=json.loads(pre_train["relative_position"][index])

      # 根据模型进行预测
      X=np.array([vec])
      yhat = model.predict(X, verbose=0)
      pre_position=[yhat[0][0]*1500-750,yhat[0][1]*1500-750]

      print("pre_position",pre_position)

      centroid1=self.getPt(Polygon(poly1).centroid)
      centroid2=self.getPt(Polygon(poly2).centroid)
      vec_now=[centroid2[0]-centroid1[0],centroid2[1]-centroid1[1]]
      poly3=GeoFunc.getSlide(poly2,pre_position[0]-vec_now[0],pre_position[1]-vec_now[1])
      GeoFunc.getSlide(poly2,position[0]-vec_now[0],position[1]-vec_now[1])

      PltFunc.addPolygon(poly1)
      PltFunc.addPolygon(poly2)

      vec=self.getFeasible(poly1,poly3)
      GeoFunc.slidePoly(poly3,vec[0],vec[1])
      PltFunc.addPolygonColor(poly3)
      PltFunc.showPlt()
   
   def getFeasible(self,poly1,poly2):
      sliding=GeoFunc.copyPoly(poly2)
      nfp=NFP(poly1,sliding)
      locus=poly2[nfp.locus_index]
      _min={
         "edge":[],
         "distance":9999999,
         "vec":[]
      }
      edges=GeoFunc.getPolyEdges(nfp.nfp)
      for edge in edges:
         distance,vec=GeoFunc.pointLineDistance(locus,edge)
         if distance<_min["distance"]:
            _min["distance"]=distance
            _min["edge"]=edge
            _min["vec"]=vec
      return _min["vec"]

   def trainModel(self,x_val,y_val,x_train,y_train):
      '''
      训练模型
      '''
      print('Build ------------')
      model = Sequential()

      model.add(layers.Dense(512, activation='sigmoid', input_shape=(512,)))

      model.add(layers.Dense(256, activation='sigmoid'))

      model.add(layers.Dense(128, activation='sigmoid'))

      model.add(layers.Dense(64, activation='sigmoid'))
      
      model.add(layers.Dense(8, activation='sigmoid'))

      # model.compile(loss='categorical_crossentropy', optimizer="rmsprop", metrics=['accuracy']) 
      model.compile(loss='mean_squared_error', optimizer="rmsprop", metrics=['accuracy']) 

      # 使用fit()来训练网路
      print('Training ------------')
      history = model.fit(x_train, y_train, epochs=4000, batch_size=256,validation_data=(x_val, y_val))
      
      model.save("/Users/sean/Documents/Projects/Packing-Algorithm/model/256.h5")
      # model.save("/Users/sean/Documents/Projects/Packing-Algorithm/model/mse_epoch_250_sample_5000_rmsprop_128_64_batch_256.h5")

      print('Plot ------------')
      import matplotlib.pyplot as plt

      history_dict = history.history

      self.storeResult(history_dict)
      
      '''
         损失值判断
      '''
      val_loss_values = history_dict['val_loss']
      loss_values = history_dict['loss']
      epochs = range(1, len(loss_values) + 1)     
      plt.plot(epochs, loss_values, 'bo', color='#A6C8E0',label='Training loss')
      plt.plot(epochs, val_loss_values, 'b', color='#A6C8E0',label='Validation loss')
      plt.title('Training and validation loss')
      plt.xlabel('Epochs')
      plt.ylabel('Loss')
      plt.legend()
      plt.show()

      plt.clf()

      '''
         准确性
      '''
      acc = history.history['accuracy']
      epochs = range(1, len(acc) + 1)
      val_acc = history.history['val_accuracy']
      plt.plot(epochs, acc, 'bo', color='#A6C8E0',label='Training acc')
      plt.plot(epochs, val_acc, 'b', color='#A6C8E0',label='Validation acc')
      plt.title('Training and validation accuracy')
      plt.xlabel('Epochs')
      plt.ylabel('Accuracy')
      plt.legend()
      plt.show()
   
   def storeResult(self,history_dict):
      '''
      存储最终的训练结果
      '''
      with open("/Users/sean/Documents/Projects/Packing-Algorithm/model/record/"+time.asctime(time.localtime(time.time()))+"result.csv","a+") as csvfile: 
         writer = csv.writer(csvfile)
         for i in range(len(history_dict["loss"])):
            writer.writerows([[history_dict["accuracy"][i],history_dict["val_accuracy"][i],history_dict["loss"][i],history_dict["val_loss"][i]]])
   
   def getPt(self,point):
      mapping_result=mapping(point)
      return [mapping_result["coordinates"][0],mapping_result["coordinates"][1]]

   
if __name__ == '__main__':
   tm=trainModel()
   # tm.dataLoad()
   # tm.trainModel()
   # tm.modelRealTest()
   tm.testModelFour()