#!/usr/bin/python3

#TODO: change if/else logic to catch end of list

two_d_list=[]
for line in open(0):
    list_1=[]
    line=line.split()[0]
    for i in range(len(line)):
        list_1.append(int(line[i]))
    two_d_list.append(list_1)


count = len(two_d_list) * 2 + (len(two_d_list) - 2)*2
factorlist=[]
for i in range(1,len(two_d_list)-1):
    for j in range(1, len(two_d_list)-1):
        count=0
        broke=False
        for k in  range(j-1,-1,-1):
            broke=True
            count+=1
            if two_d_list[i][j] <= two_d_list[i][k]:
                break
        if(not broke):
            count=1
        factor=count

        count=0
        broke=False
        for k in range (j+1,len(two_d_list)):
            broke=True
            count+=1
            if two_d_list[i][j] <=  two_d_list[i][k]:
                break
        if(not broke):
            count=1
        factor*=count
            
        count=0
        broke=False
        for k in range (i-1,-1,-1):
            broke=True
            count+=1
            if two_d_list[i][j] <=  two_d_list[k][j]:
                break
        if(not broke):
            count=1
        factor*=count

        count=0
        broke=False
        for k in range (i+1,len(two_d_list)):
            broke=True
            count+=1
            if two_d_list[i][j] <=  two_d_list[k][j]:
                break
        if(not broke):
            count=1
        factor*=count
            
            
        factorlist.append(factor)
print(max(factorlist))