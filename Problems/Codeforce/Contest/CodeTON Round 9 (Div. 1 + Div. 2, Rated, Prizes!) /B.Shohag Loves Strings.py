
from collections import Counter
from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():
    s=input()
    if(len(s)==1):
        return [-1]
    if(len(s)==2):
        if(s[0]==s[1]):
            return s
        else:
             return [-1]

    sub=s[:3]
    size=len(s)
    a=Counter(sub)
    m=len(a)
    #print(m)
    
    if(m==3):
        return sub
    elif(m==2):
        if(s[0]==s[1]):
              return s[:2]
        elif(s[1]==s[2]):
              return [s[1],s[2]]
        else:
            if(size<=3):
                return [-1]
            for aux in range(0,size-3,1):
                if(s[aux+3]!=s[aux+1]):
                    #print("as")
                    if(s[aux+3]==s[aux+2]):
                        return [s[aux+2],s[aux+3]]
                    else:
                        return [s[aux+1],s[aux+2],s[aux+3]]      
            return [-1]
    elif(m==1):
        return s[:2]
	

t=1
t=int(input())
for i in range(t):
    for j in solve():
        print(j,end='')
    print()
	
