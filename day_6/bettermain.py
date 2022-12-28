#!/usr/bin/python3

inrec=input()

for i in range(4,len(inrec)):
    if(len(set(inrec[i-4:i]))>3):
        print(i)
        break