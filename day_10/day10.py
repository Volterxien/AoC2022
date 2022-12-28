#!/usr/bin/python3


CHECK_VALUE=20
cycle=0
x=1
sum=0
count=0
DIVISOR=40
dot="."
hash="#"

def check():
    global CHECK_VALUE, sum

    if cycle == CHECK_VALUE:
        sum=sum + x*CHECK_VALUE
        CHECK_VALUE+=40
      
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
    check()
    if(len(line)==2):
        print_char()
        cycle+=1
        count+=1
        check()
        x+=int(line[-1])

print()
print(sum)
        
        