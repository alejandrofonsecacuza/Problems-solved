
#dict(zip(lista,map(lambda x: lista.count
#lista=[1,1,2,3,4,5,4]
def solve(lista):
    return len((list(filter(lambda x: lista.count(x)>1,lista))))//2
				
				
t=int(input())
while t:
	_=int(input())
	lista=list(map(int,input().split()))
	print(solve(lista))
	t-=1
			    