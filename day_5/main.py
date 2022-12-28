#!/usr/bin/python3

container=[]
stack=[]
stack_init_state=False
stack_build_state=False

def init_stack(line):
    for j in range(len(line)//4):
        stack.append([])


def build_stack(line):
    global stack_init_state 
    if (stack_init_state is False):
        init_stack(line) 
        stack_init_state= True
    for i in range(len(line)):
        if line[i].isalpha():
            stack[i//4].insert(0,line[i])

def do_work(line):
    if(line[0]== '\n'):
        return
    res=[int(i) for i in line.split() if i.isdigit()]
    for i in range(res[0]):
        stack[res[2]-1].append(stack[res[1]-1].pop())

def print_result():
    for i in range(len(stack)):
        print(stack[i][len(stack[i])-1], end='')
    print()

for line in open(0):
    if(line[0] == '\n'):
        stack_build_state =True
    if(stack_build_state is False):
        build_stack(line)
    else:
        do_work(line)

print_result()