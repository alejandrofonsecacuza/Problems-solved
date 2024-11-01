while(True):
	a,b=map(int,input().split())
	if(a==-1 and b==-1):
		break
	print( min(abs(b-a),100-abs(b-a)))

