from math import ceil,floor
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n,a,b,c=cinline()
    k=a+b+c
    arr=(a,b,c)
    aux=floor(n/k)*k
    result=floor(n/k)*3
    index=0
    while(aux<n):
        aux+=arr[index]
        index+=1
        index%=3
        result+=1
    return result
t=1
t=cinint()
for _ in range(t):
    print(solve())