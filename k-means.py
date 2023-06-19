# from math import *

# def clustering(a):
#     global c,lists
#     dis=[sqrt((c[0][0]-a[0])**2+(c[0][1]-a[1])**2),
#          sqrt((c[1][0]-a[0])**2+(c[1][1]-a[1])**2),
#          sqrt((c[2][0]-a[0])**2+(c[2][1]-a[1])**2)]
#     minimum=min(dis)
#     for j in range(len(dis)):
#         if dis[j]==minimum:
#             c[j]=((c[j][0]+a[0])/2,(c[j][1]+a[1])/2)
#             lists[j].append(a)
#             return j

# datapoints=[(1.713,1.586),
#             (0.180,1.786),
#             (0.353,1.240),
#             (0.940,1.566),
#             (1.486,0.759),
#             (1.266,1.106),
#             (1.540,0.419),
#             (0.459,1.799),
#             (0.773,0.186)]
# c=[(1.678,1.712),
#    (0.809,1.349),
#    (1.112,1.679)]

# lists=[[],[],[]]

# for i in datapoints:
#     clustering(i)

# print(lists)
# #x=(0.906,0.606)
# val=float(input("x :")),float(input("y :"))
# print("Clustered in centroid : ",clustering(val))
# print(lists)
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import datasets
diabetes=datasets.load_diabetes()
print(diabetes)
diabetes_x=diabetes.data[:,np.newaxis,2]
diabetes_x_train=diabetes_x[:-30]
diabetes_x_test=diabetes_x[-30:]

diabetes_y_train=diabetes.target[:-30]
diabetes_y_test=diabetes.target[-30:]
print(diabetes_x_train)
# plt.scatter(diabetes_x_train,diabetes_y_train)
# plt.show()
mean_x=np.mean(diabetes_x_train)
mean_y=np.mean(diabetes_y_train)
m=len(diabetes_x_train)
numer=0
denom=0
for i in range(m):
    numer+=((diabetes_x_train[i])-mean_x)*((diabetes_y_train[i])-mean_y)
    denom+=((diabetes_x_train[i])-mean_x)**2
b1=numer/denom
b0=mean_y-(b1*mean_x)
print(b1,b0)
plt.scatter(diabetes_x_test,diabetes_y_test,c="blue",label="ScatterPlot")
# plt.plot(diabetes_x_test,)
plt.xlabel("Data")
plt.ylabel("Target")
plt.legend()
plt.show()