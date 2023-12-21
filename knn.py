from math import *
dist_0=[]
dist_1=[]
print("Helooooooooooooo")

def calculate_0(x,p):
    for i in x:
        dist=sqrt((p[0]-i[0])**2+(p[1]-i[1])**2)
        dist_0.append(dist)

def calculate_1(x,p):
    for i in x:
        dist=sqrt((p[0]-i[0])**2+(p[1]-i[1])**2)
        dist_1.append(dist)

p=(1,0)
points_0=[(2,1),(2,1),(1,0),(2,2)]
points_1=[(0,1),(1,2),(1,0),(0,0),(2,0),(1,2),(0,2)]

calculate_0(points_0,p)
calculate_1(points_1,p)

final_list=dist_0+dist_1

sort_dist=sorted(final_list)

count_0=0
count_1=0

for i in range(len(sort_dist)):
    if sort_dist[i] in dist_0:
        count_0+=1
    if sort_dist[i] in dist_1:
        count_1+=1
    if count_0>=3 or count_1>=3:
        break

if count_0>count_1:
    print("Belongs to 0 label")
else:
    print("Belongs to 1 label")
