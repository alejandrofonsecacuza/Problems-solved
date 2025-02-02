def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))

def solve():
    h,w,n=cinline()
    f=lambda x:1 if ((x//w)*(x//h))>=n else 0
    low = 0
    high = h*w*n
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if not f(mid):
            low = mid + 1
        else:
            high = mid - 1
    return low
    
    
t=1
#t=cinint()
for _ in range(t):
    print(solve())