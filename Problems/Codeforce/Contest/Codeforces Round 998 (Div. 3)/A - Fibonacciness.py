def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
from collections import defaultdict,Counter
def solve():
    counter=defaultdict(int)
    a1,a2,a4,a5=cinline()
    counter[a1+a2]+=1
    counter[a4-a2]+=1
    counter[a5-a4]+=1
    
    return Counter(counter).most_common(1)[0][1]
    
    
    
    pass
t=1
t=cinint()
for _ in range(t):
    print(solve())