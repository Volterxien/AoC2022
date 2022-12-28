#!/usr/bin/python3
container=[]
stack=[]
flag = False
for line in open(0):
    for i in range(len(line)):
        if flag is False:
            for j in range(len(line)//4):
                stack.append([])
            flag=True
        if line[i].isalpha():
            stack[i//4].append(line[i])

print(stack)