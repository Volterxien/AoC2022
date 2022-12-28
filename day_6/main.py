#!/usr/bin/python3

inrec=""
with open(0) as f:
    inrec=f.read()
count=4
if(len(set(inrec[0:4]))>3):
    print(count)
    exit

for i in range(0,len(inrec)-3):
    if(len(set(inrec[i:(i+4)]))>3):
        break
    count+=1

print(count)
# str1="abcd"
# str2="d"
# print(set(str1)&set(str2))