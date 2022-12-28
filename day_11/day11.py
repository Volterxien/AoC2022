#!/usr/bin/python3.10

import string
from enum import Enum
import re

plus=0
minus=1
times=2

item_list=0
operation=1
factor=2
divisor=3
true=4
false=5


monkeys=[]

for line in open(0):
    monkey=[]
    line=re.sub('[^\w\s+*-]','', line).split()
    if(len(line)>0):
        match line[0]:
            case 'Monkey':
                monkey_num=int(line[1])
                monkeys.append(monkey)
            case "Starting":
                index=-1
                monkey_items=[]
                while line[index][item_list][0].isdigit(): 
                    monkey_items.append(int(line[index]))
                    index-=1
                monkeys[monkey_num].append(monkey_items)
            case "Operation":
                match line[-2]:
                    case '+':
                        monkeys[monkey_num].append(plus)
                    case '-':
                        monkeys[monkey_num].append(minus)
                    case '*':
                        monkeys[monkey_num].append(times)
                if line[-1][0].isdigit():
                    monkeys[monkey_num].append(int(line[-1]))
                else:
                    monkeys[monkey_num].append(-1)
            case "Test":
                monkeys[monkey_num].append(int(line[-1]))
            case "If":
                if line[1]=="true":
                    monkeys[monkey_num].append(int(line[-1]))
                else:
                    monkeys[monkey_num].append(int(line[-1]))
    


monkey_business=[0]*len(monkeys)

for _ in range(20):
    for i in range(len(monkeys)):

                
        count=0
        for _ in range(len(monkeys[i][item_list])):
            
            if monkeys[i][factor] == -1:
                num=monkeys[i][item_list].pop(0)
                if monkeys[i][operation] == minus:
                    num=num-num
                elif monkeys[i][operation] == plus:
                    num=num+num
                else:
                    num=num*num
                
            else:
                if monkeys[i][operation] == minus:
                    num=monkeys[i][item_list].pop(0) - monkeys[i][factor]
                elif monkeys[i][operation] == plus:
                    num=monkeys[i][item_list].pop(0) + monkeys[i][factor]
                else:
                    num=monkeys[i][item_list].pop(0) * monkeys[i][factor]
            
            num=num//3

            if num % monkeys[i][divisor]== 0:
                sendto=monkeys[i][true]
            else:
                sendto=monkeys[i][false]
            monkeys[sendto][item_list].append(num)
            count+=1
        monkey_business[i]+=count
        

max1=max(monkey_business)
monkey_business.remove(max1)
print(max1*max(monkey_business))

