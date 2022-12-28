import string
import re

print(string.punctuation)
mystr=string.punctuation
mystr=mystr.strip('+-*')
print(mystr)

teststr="!@#$%^&*()?+-"
teststr=re.sub('[^\w+*-]','', teststr)
print(teststr)