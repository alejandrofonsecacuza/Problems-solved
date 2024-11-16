def cinline():
	return list(map(int,input().split()))

while(True):
	try:
		N,B,H,W=cinline()
	except:
		break
	HOTELS=[]
	
	for i in range(H):
		m=int(input())
		a=cinline()
		a.append(m)
		HOTELS.append(a)
	HOTELS=sorted(HOTELS,key=lambda x:x[-1])
	band=False
	for i in HOTELS:
		if(max(i[:-1])>=N):
			if((i[-1]*N)<=B):	
				print(i[-1]*N)
				band=True
				break
		
	if(not band):
		print("stay home")					
