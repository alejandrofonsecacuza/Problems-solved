def cinint():
    return int(input())
def cinline():
    return list(map(int,input().split()))
def solve():
    n,m=cinline()
    cards=dict()
    for c in range(n):
        for i in cinline():
            cards[i]=c
    #print(f'{cards=}')
    drops_cow=list()
    path=[]
    already=False
    for index in range(n*m):
        
        #print(f'{index=}')
        drop=cards[index]
        #print(f'{cards[index]=}')
        if already:
            #print(f'error {drop=} -- {path[index%n]=} ')
            if drop != path[index%n]:
                return [-1] 
        if drop in drops_cow:
            return [-1]
        else:
            drops_cow.append(drop)
        #print(f'{drops_cow=}')
        if len(drops_cow)==n:
            if not already:
                path=drops_cow.copy()
                #print(f'{path=}')
            already=True
            drops_cow=list()
            
    
    return list(map(lambda x:x+1,path))
t=1
t=cinint()
for _ in range(t):
    print(*solve())