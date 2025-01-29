
def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def f(n):
    return (n*(n+1))/2
def solve():
    n=int(input())
    aux=f(n)
    if(aux%2!=0):
        print("NO")
        return
    aux/=2
    set1=[]
    set2=[]  
    for i in range(n,0,-1):
        #print(1,aux)
        if(i<=aux):
            set1.append(i)
            aux-=i
        else:
            set2.append(i)
    print("YES")
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
    return
t=1
#t=cinint()
for _ in range(t):
    (solve())