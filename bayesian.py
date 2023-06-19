def doc_split(name):
    
    with open(name,'r') as file:
        doc=[i.strip() for i in file]
    return [i.split() for i in doc]

def vec_cal(doc):
    lis=[]
    for i in final_list:
        lis.append(doc.count(i))
    return lis

def prob(vec,val):
    p=len(class_label[val])/len(l)
    for i in vec:
        sum=0
        ind=final_list.index(i)
        for x in class_label[val]:
            sum+=vector[x][ind]
        if sum==0:
            sum=(0+len(l)*(1/2))/(len(class_label[val])+len(l))
        p=p*(sum/len(class_label[val]))
    return p

l=[]
final_list=[]
#0 index for question and 1 index for answers
class_label=[[],[]]
n=int(input("Enter no of files to read :"))
for i in range(n):
    print("Enter name of file -",i+1," :",end="")
    name=input()
    x=int(input("1.Question text\n2.Answer text\nEnter your choice:"))
    class_label[x-1].append(i)
    l.extend(doc_split(name))
    for x in l[i]:
        final_list.append(x)
final_list=sorted(set(final_list))
vector=[]
for i in l:
    vector.append(vec_cal(i))

file=input("Enter name of test file : ")
file=doc_split(file)
print("Unique words are:",final_list)
print("vector for given:",file,"is\n",vec_cal(file[0]))
print("Question files are :",len(class_label[0]),"\nAnswer files are :",len(class_label[1]))
qp=prob(file[0],0)
ap=prob(file[0],1)
if qp>ap:
    print("The given file is a Question")
else:
    print("The given file is an answer")