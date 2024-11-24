from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def solve():

    k=cinint()
        
    j=1
    response=[]
    for x in range(2,100):
        if(x-(j-1))%j==0:
            response.append(x)
            j+=1
            if(len(response)==k):
                  return response

	

			
	

t=1
t=int(input())
for i in range(t):
	print(*solve())
	
