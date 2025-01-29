def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()#n>=6
    response=[1,1]
    for i in range(2,3000):
        if(len(response)!=n-1):
            response.append(i)
        else:
            break
    response.append(1)
    return response
t=1
t=cinint()
for _ in range(t):
    print(*solve())