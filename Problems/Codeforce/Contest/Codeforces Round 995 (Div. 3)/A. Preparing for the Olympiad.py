def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n=cinint()
    mono=cinline()
    stere=cinline()

    stere.append(0)
    result=0
    for i in range(len(mono)):
        if(mono[i]>stere[i+1]):
            result+=mono[i]-stere[i+1]
    return result        
        
    pass
t=1
t=cinint()

for _ in range(t):
    print(solve())