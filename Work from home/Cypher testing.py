from math import log2
from random import randint

def cypher(text,multiplier):
    for i in range(len(text)):
        s=text[i]
        s=ord(s)
        if (type(log2(s)) == int):
            s=(s//2)+200
        else:
            s=(3*s)+101
        s=str(s)
        to_copy.write(s)
        for i in range(len(s)):
            encoding=int(s[i])*multiplier
            to_copy.write(chr(encoding+100))
w=(randint(0,1000))
v=(randint(0,1000))
u=(randint(0,1000))
encode=w+v+u
encode=str(encode)
i=0
encoded=[]
while i<len(encode)-1:
    print((int(encode[i])%2==0))
    print(int(encode[i+1])%2==0)
    if(((int(encode[i])%2==0)^(int(encode[i+1])%2==0))==1):
        encoded.append(encode[i])
    else:
        encoded.append(encode[i+1])
    i+=1
encoded=str(encoded).replace("'","").replace("[","").replace("]","").replace(",","").replace(" ","")
encoded=int(encoded)
text=input("Enter some text \n")
to_copy = open("Cypher.txt","w", encoding="utf-8")
cypher(text,encoded)
to_copy.close()
