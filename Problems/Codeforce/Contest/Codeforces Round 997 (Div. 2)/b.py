def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    M=[]
    
    for _ in range(n):
        M.append(list(map(int,list(input()))))
   # print(f'{M=}')
    response=[-1]*n
    for v in range(n,0,-1):
    #    print(f'{v=}')
        index=sum(M[v-1][:v-1])
        for j in range(len(response)):
            if response[j]!=-1:
                continue
            if index==0:
                response[j]=v
                break
            if(response[j]==-1):
                index-=1
    return response
t=1
t=cinint()
for _ in range(t):
    print(*solve())