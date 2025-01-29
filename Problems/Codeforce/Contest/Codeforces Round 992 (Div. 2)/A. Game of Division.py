def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n,k=cinline()
    a=cinline()
    for  index,value in enumerate(a):
       #print(f"{value=}")
        band=True
        for index2,value2 in enumerate(a):
        #    print(f"{value2=}")
            if(index==index2):continue
            if(abs(value-value2)%k==0):
                band=False
                break
        if(band):
            return index+1
    return -1    

        
t=1
t=cinint()
for _ in range(t):
    response=solve()
    if(response==-1):
        print("NO")
    else:
        print("YES")
        print(response)

