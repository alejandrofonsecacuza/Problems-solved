def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n,m=cinline()
    response=0
    l=[]
    for _ in range(n):
        l.append(list(input()))
    for aux in l:        
        if len(aux) <= m:
            response+=1
            m-=len(aux)
        else:
            return response
    return response

t=1
t=cinint()
for _ in range(t):
    print(solve())