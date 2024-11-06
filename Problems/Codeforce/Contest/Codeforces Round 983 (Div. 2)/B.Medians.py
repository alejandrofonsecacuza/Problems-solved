from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))
def solve():
    n,k=cinline()
    if(n==1):
        print(1)
        print(1)
    else:
        if(k==n or k==1):
            print(-1)
        else:
            if(k%2==0):
                print(3)
                print(1,k,k+1)
            else:
                print(5)
                print(1,2,k,k+1,k+2)
                
                
 
    
t=int(input())
for i in range(t):
    solve()
