count=0

for line in open(0):
    k=line.split(',')
    ab,cd=[(int(x),int(y)) for x,y in (pair.split('-') for pair in k)]
    # if(a<=c):
    #     if(b>=d):
    #         count+=1
    #        # print(a,b,c,d)
    # elif(c<=a):
    #     if(d>=b):
    #         count+=1
    #         #print(a,b,c,d)
    # if(cd[0] in range(ab[0],ab[1]) and cd[1] in range(ab[0],ab[1])):
    #     count+=1
    #     print("found")
    #     print(ab,cd)
    # elif(ab[0]  in range (cd[0], cd[1]) and ab[1] in range(cd[0], cd[1])):
    #     count+=1
    #     print("found")
    #     print(ab,cd)
    # if((range(ab[0], ab[1]))).issubset(range(cd[0],cd[1])):
    #     count+=1
    if(ab[0]<=cd[0] and ab[1]>=cd[1] ):
        count+=1
    elif(ab[0]>=cd[0] and ab[1] <= cd[1]):
        count+=1

print(count)
