import numpy as np
import matplotlib.pyplot as plt
# 回归，有监督学习，X，y
X = np.random.rand(100, 1)
print("ex",X)
# y模拟出来真实数据，也就是y_hat 和error
y = 5 + 4 * X + np.random.randn(100, 1)
# c_表示连接，为了求W0截距，加上一个全为1的XO
X_b = np.c_[np.ones((100, 1)), X]
# 实现公式来解θ θ = (x^x)^-1*x^T*y  这里的.T就是 transpose 转置的作用，
# dot 就是向量点乘， np.linalg.inv是矩阵求逆
θ = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print("theta",θ)
# 创建一个模型做预测
X_new = np.array([
    [0],
    [2]
])
X_new_b = np.c_[np.ones((2, 1)), X_new]
print("xn",X_new_b)
y_predict = X_new_b.dot(θ)
print("yp",y_predict)
plt.plot(X_new, y_predict, 'r-')
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()
# ————————————————
# 版权声明：本文为CSDN博主「__Songsong」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_45316122/article/details/102841123