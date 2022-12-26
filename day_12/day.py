#!/usr/bin/python3

import pdb

arr2d=[]
start=[]
end=[]
d1=0
found_start=False
found_end=False
for line in open(0):
    arr2d.append(line.strip())


for i in range(len(arr2d)):
    d2=0
    for j in arr2d[i]:
        if found_start is True and found_end is True:
            break
        if j == "S":
            found_start =True
            start=[d1,d2]
        elif j == "E":
            end=[d1,d2]
            found_end=True
        d2+=1
    d1+=1
    
    if found_end is True and found_start is True:
        break


print(start,end)
while start != end:
    print(start,end)
    if start[0]<end[0]:
        start[0]+=1
    if start[1]<end[1]:
        start[1]+=1
