def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    return sum(list(map(int,list(input()))))
t=1
t=cinint()
for _ in range(t):
    print(solve())