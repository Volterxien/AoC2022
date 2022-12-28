#!/usr/bin/python3 

mydict={}
mylist=list()
count=[]
sum=0
totalsum=0
MAXSIZE=70000000
NEEDED_SPACE=30000000
for line in open(0):
    if(line[2:4] == "cd"):
        #Going back one directory -> update dictionary, pop sum, add totalsum
        if(line[5:-1] == ".."):
            mydict[mylist.pop()]=sum
            if(sum<100000):
                totalsum=totalsum+sum
            sum=sum+count.pop()

        #Entering new directory -> push sum to list
        #                       -> push directory name to list
        else:
            count.append(sum)
            sum=0
            mylist.append(line[5:-1])
    if line[0].isdigit():
        sum=sum+int(line.split()[0])
        continue

#UPdate dictionary until at root dir
for i in range(len(mylist)):
    mydict[mylist.pop()]=sum
    sum=sum+count.pop()

space=MAXSIZE-mydict.get("/")

#Use min() instead of this
good_key="/"
for key in mydict:
    if space + mydict.get(key) > NEEDED_SPACE and mydict.get(good_key) > mydict.get(key):
        good_key=key

print(mydict.get(good_key))
print(totalsum)