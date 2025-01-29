def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    if(n==1):
        return 1
    if(n>=2 and n<=4):
        return 2
    index=1
    aux=2
    while(True):
        #print(f"{aux=}")
        if(aux>n):
            return index
        index+=1
        aux=(aux*2)+1
t=1
t=cinint()
for _ in range(t):
    print(solve())