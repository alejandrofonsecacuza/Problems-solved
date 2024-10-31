def solve(a,ns):
    minor=min(a)
    for i in ns:
        if(i<minor):
            print(i)
        else:
            print(minor-1)
    


t=int(input())
while(t):
	k,q=map(int,input().split())
	a=list(map(int,input().split()))
	ns=list(map(int,input().split()))
	solve(a,ns)
	t-=1
	
