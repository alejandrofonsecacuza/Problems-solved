def solve():
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    for index,num in enumerate(l):
        if(index+1!=num):
            return (index+1)
    return n
t=1;
while(t):
    print(solve())
    t-=1
