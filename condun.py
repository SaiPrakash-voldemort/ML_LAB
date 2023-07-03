import pandas as pd
def conditional():
    for i in range(len(col)):
        print(i+1,".",col[i])
    a1=int(input("enter attribute 1 : "))
    l1=[]
    for i in range(len(dataset[col[a1-1]])):
        if dataset[col[a1-1]][i] not in l1:
            l1.append(dataset[col[a1-1]][i])
    for i in range(len(l1)):
        print(i+1,".",l1[i])
    a1_value=int(input("enter:"))
    temp1=l1[a1_value-1]
    for i in range(len(col)):
        print(i+1,".",col[i])
    a2=int(input("enter attribute 2 : "))
    l2=[]
    for i in range(len(dataset[col[a2-1]])):
        if dataset[col[a2-1]][i] not in l2:
            l2.append(dataset[col[a2-1]][i])
    for i in range(len(l2)):
        print(i+1,".",l2[i])
    a2_value=int(input("enter:"))
    temp2=l2[a2_value-1]
    count1=0
    count2=0
    length=len(dataset[col[a2-1]])
    for i in range(len(dataset[col[a1-1]])):
        if (temp1==dataset[col[a1-1]][i]):
            count1=count1+1
        if(temp1==dataset[col[a1-1]][i] and temp2==dataset[col[a2-1]][i]):
            count2=count2+1
    prob_attr1=count1/len(dataset[col[a1-1]])
    prob_attr2=count2/len(dataset[col[a2-1]])
    print("conditional probability of ",temp2," given ",temp1," is :",prob_attr2,"/",prob_attr1,"=",round(prob_attr2/prob_attr1,2))


def unconditional():
    for i in range(len(col)):
        print(i+1,".",col[i])
    attr=int(input("enter:"))
    l1=[]
    for i in range(len(dataset[col[attr-1]])):
        if dataset[col[attr-1]][i] not in l1:
            l1.append(dataset[col[attr-1]][i])
    for i in range(len(l1)):
        print(i+1,".",l1[i])
    attr_value=int(input("enter:"))
    temp1=l1[attr_value-1]
    count=0
    for i in range(len(dataset[col[attr-1]])):
        if(temp1==dataset[col[attr-1]][i]):
            count=count+1
    print("unconditional probability of ",temp1,"is :",count,"/",len(dataset[col[attr-1]]),"=",count/len(dataset[col[attr-1]]))
        
dataset=pd.read_csv("C:/Users/dhanr/Documents/LABS/MLKTR/SRIDHAR/dataset.csv")
col=list(dataset.columns)
print("1.unconditional.\n2.conditional.")
n=int(input("enter : "))
if(n==1):
    unconditional()
elif(n==2):
    conditional()
else:
    pass