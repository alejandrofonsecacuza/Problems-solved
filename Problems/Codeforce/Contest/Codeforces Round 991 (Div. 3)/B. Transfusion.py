def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    a=cinline()
    sum_even=0
    sum_odd=0
    
    
    sum_even=sum([a[item] for item in range(0,n,2)])
    sum_odd=sum([a[item] for item in range(1,n,2)])
    if((sum_even+sum_odd)%n!=0):
        return "NO"
    count_odd=n//2
    count_even=n-count_odd
    
    
    return "YES" if (sum_even/count_even)==(sum_odd/count_odd) else "NO"

t=1
t=cinint()
for _ in range(t):
    print(solve())