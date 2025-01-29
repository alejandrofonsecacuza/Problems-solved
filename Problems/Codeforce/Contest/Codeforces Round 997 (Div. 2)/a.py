
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n,m=cinline()
    sum_x=0
    sum_y=0
    
    arr=[]
    for _ in range(n):
        x,y=cinline()
        sum_x+=x
        sum_y+=y
        arr.append((x,y))
    #print(f'{sum_x=}')
    #print(f'{sum_y=}')
    return ((sum_x+m-arr[0][0])*2)+((sum_y+m-arr[0][1])*2)
        
t=1
t=cinint()
for _ in range(t):
    print(solve())