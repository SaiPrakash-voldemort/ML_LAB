import pandas as pd
import matplotlib.pyplot as plt
def fun(x,y):
    lis=[]
    for i in range(len(dataset[col[x]])):
        lis.append((dataset[col[x]][i]-mean[x])*(dataset[col[y]][i]-mean[y]))
    return sum(lis)
dataset=pd.read_csv("Book1.csv")
col=list(dataset.columns)
x,y=0,1
mean=[sum(dataset[col[x]])/len(dataset[col[x]]),sum(dataset[col[y]])/len(dataset[col[y]])]
b1=fun(x,y)/fun(x,x)
b0=mean[y]-b1*mean[x]
print("b0 : ",b0,"b1 :",b1)
lis=[]
x1=float(input("Enter x value : "))
print("y value is :",b0+b1*x1)
for i in dataset[col[x]]:
    lis.append(b0+b1*i)
plt.scatter(dataset[col[x]],dataset[col[y]])
plt.plot(dataset[col[x]],lis,color="black")
plt.scatter(x1,b0+b1*x1)
plt.show()
