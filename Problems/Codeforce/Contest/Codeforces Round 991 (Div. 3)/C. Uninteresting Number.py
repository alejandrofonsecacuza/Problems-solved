from math import ceil
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
from collections import Counter
def solve():
    n=list(map(int,list(input())))
    cnt=Counter(n)
    #print(f'{sum(n)=}')
    sum_n=sum(n)
    r=sum(n)%9
    count_3=cnt[3]
    count_2=cnt[2]
    if r==0:
        return "YES"
    m=0
    if r%2==0:
        m=18-r
    else:
        m=9-r
    x=(m/2)//3
    x=min(x,count_3)
    y=(m/2)-(3*x)
    if y<=count_2:
        return "YES"
    else:
        return "NO" 
t=1
t=cinint()
for _ in range(t):
    print(solve())