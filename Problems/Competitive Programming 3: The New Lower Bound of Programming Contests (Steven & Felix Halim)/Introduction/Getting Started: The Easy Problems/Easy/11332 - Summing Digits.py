def back(n):
	global sum_total
	if(len(str(n))==1):
		print(n)
		return
	sum=0
	for i in str(n):
		sum+=int(i)
	back(sum)
	


while(True):
	global sum_total

	n=int(input())
	if(n==0):
		break
	back(n)
	


