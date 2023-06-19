import pandas as pd

def index_finder(list1,val1):
    list2=[]
    for i in range(len(list1)):
        if list1[i]==val1:
            list2.append(i)
    return list2

def find_unique(l):
    list1=[]
    for i in l:
        if i not in list1:
            list1.append(i)
    return list1
def print_statements(l):
    for i in range(len(l)):
        print(i+1,".",l[i])
    val=int(input("Enter your choice : "))
    return val-1

def unconditional():
    attribute=print_statements(lis)
    temp=lis[attribute]
    values=find_unique(data[temp])
    val=print_statements(values)
    temp2=values[val]
    c=index_finder(data[temp],temp2)
    print(len(c),"/",len(data),":",len(c)/len(data))


def conditional():
    attribute1=print_statements(lis)
    temp1=lis[attribute1]
    values=find_unique(data[temp1])
    val=print_statements(values)

    list_1=index_finder(data[temp1],values[val])
    attribute2=print_statements(lis)
    temp2=lis[attribute2]
    values2=find_unique(data[temp2])

    val2=print_statements(values2)

    list_2=data[temp2]
    count=0
    for i in range(len(list_1)):
        x=list_1[i]
        if list_2[x]==values2[val2]:
            count+=1
    list_2=index_finder(list_2,values2[val2])
    print(count,"/",len(list_2),":",count/len(list_2))


#reading dataset
data=pd.read_csv("dataset.csv")

#making columns of dataset as a list
lis=list(data.columns)

print("1.Unconditional Probablity")
print("2.Conditional Probability")

val=int(input("Enter your choice : "))

if val==1:
    unconditional()
elif val==2:
    conditional()
else:
    print("Invalid")
