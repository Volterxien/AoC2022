#!/usr/bin/python3

DIVISOR=40
cycle=0
x=1
hash="#"
dot="."
count=0



def print_char():
    global count
    if(count%DIVISOR == 0):
        print()
        count=0
    if count in range(x-1,x+2):
        print(f'{hash}', end='')
    else:
        print(f'{dot}', end='')
 
for line in open(0):
    line=line.split()
    print_char()
    cycle+=1
    count+=1
    if(len(line)==2):
        print_char()
        cycle+=1
        count+=1
        x+=int(line[-1])

print()

        
        