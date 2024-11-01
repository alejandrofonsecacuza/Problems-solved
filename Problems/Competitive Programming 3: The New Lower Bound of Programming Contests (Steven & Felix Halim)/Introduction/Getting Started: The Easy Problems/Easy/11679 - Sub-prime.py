def cinline():
	return list(map(int,input().split()))
while(True):
	B,N=cinline()
	if(B==0 and N==0):	
		break
	money=[-1]
	money+=cinline()
	for i in range(N):	
		a,b,c=cinline()
		money[a]-=c
		money[b]+=c
	band=True
	for i in money[1:]:
		if(i<0):
			band=False
			
	if(band):
		print('S')
	else:
		print('N')
	
