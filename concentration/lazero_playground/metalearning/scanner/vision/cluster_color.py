import pandas as pd
import seaborn as sns  #用于绘制热图的工具包
from scipy.cluster import hierarchy  #用于进行层次聚类，话层次聚类图的工具包
from scipy import cluster
import matplotlib.pyplot as plt
from sklearn import decomposition as skldec  #用于主成分分析降维的包
import random
# 下读取文件的代码
df = pd.read_csv("stream.csv", index_col=0)
# randomly sample dots.
Z = hierarchy.linkage(df.sample(n=900), method='ward', metric='euclidean')
hierarchy.dendrogram(Z, labels=df.index)
plt.show()
# 602 GB needed?