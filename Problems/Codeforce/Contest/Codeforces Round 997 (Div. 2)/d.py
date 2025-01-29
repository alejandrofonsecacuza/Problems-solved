from collections import Counter
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    b=cinline()
    #Contando los arreglos impares
    #n=5
    #n+n-2+n-4
    #5+3+1
    response=0
    for i in range(0,100000,2):
        response+=(100000-(i-1))
    return response
        
    multiplay=dict(Counter(b))
    #return multiplay
    for i in range(2,n+1,2):
        print(i)        
t=1
t=cinint()
for _ in range(t):
    print(solve())