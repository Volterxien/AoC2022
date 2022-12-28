#!/usr/bin/python3

two_d_list=[]
for line in open(0):
    list_1=[]
    line=line.split()[0]
    for i in range(len(line)):
        list_1.append(int(line[i]))
    two_d_list.append(list_1)

count = len(two_d_list) * 2 + (len(two_d_list) - 2)*2

for i in range(1,len(two_d_list)-1):
    for j in range(1, len(two_d_list)-1):
        Visible=4
        for k in range (j):
            if two_d_list[i][j] <= two_d_list[i][k]:
                Visible -=1
                break
        for k in range (j+1,len(two_d_list)):
            if two_d_list[i][j] <= two_d_list[i][k]:
                Visible -=1
                break
        for k in range (i):
            if two_d_list[i][j] <= two_d_list[k][j]:
                Visible-=1
                break
        for k in range (i+1,len(two_d_list)):
            if two_d_list[i][j] <= two_d_list[k][j]:
                Visible-=1
                break
        if Visible > 0:
            count+=1

print(count)
