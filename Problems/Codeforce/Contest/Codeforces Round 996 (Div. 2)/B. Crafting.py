def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    a=cinline()
    b=cinline()
    min_olg=float("inf")
    first_ask=False
    ask=0
    
    for index in range(n):
        #print(f'{a[index]=}')
        #print(f'{b[index]=}')
        if(a[index]<b[index]):
            if(first_ask):
                return "NO"
            ask=b[index]-a[index]
            #print(f'{ask=}')
            if(ask>min_olg):
                return "NO"
            first_ask=True     
        else:
            olg=a[index]-b[index]
            if(olg>=ask):
                min_olg=min(min_olg,(olg-ask))
            else:
                return "NO"
    return "YES"
t=1
t=cinint()
for _ in range(t):
    print(solve())