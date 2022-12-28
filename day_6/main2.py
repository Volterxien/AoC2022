#!/usr/bin/python3

inrec=""
with open(0) as f:
    inrec=f.read()
count=14
if(len(set(inrec[0:14]))>13):
    print(count)
    exit()

for i in range(0,len(inrec)-13):
    if(len(set(inrec[i:(i+14)]))>13):
        break
    count+=1

print(count)