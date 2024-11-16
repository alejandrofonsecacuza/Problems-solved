from collections import defaultdict
band=False
while(True):

	try:
		n=int(input())
		memo=defaultdict(int)
		names=input().split()
		if(band):
			print()
		band=True
	except EOFError:
		break
	
	for i in range(n):
		name,money,m,*friends=input().split()
		money=int(money)
		m=int(m)
		if m!=0:
			memo[name]-=(money-(money%m))
			for friend in friends:
				memo[friend]+=money//m
	for _ in names:
		print(_,memo[_])
	#print()
	#print()

		
