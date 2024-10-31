from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))


def solve():
	n=cinint()
	a=cinline()
	m=n//2
	if(n%2==0):

		a1=a[:m]
		a2=a[m:][::-1]
	else:
		a1=a[:m+1]
		a2=a[m+1:][::-1]
	#print(a1,a2)
	if(n%2!=0):
		a2.append(-1)
	
	result=0
	#print("m",m)
	for i in range(m-1 if n%2==0 else m):
		count=0
		
		if(a1[i]==a1[i+1] or a2[i]==a2[i+1] or (i>0 and a1[i]==a1[i-1]) or (i>0 and a2[i]==a2[i-1])):
			#print("problem",i)
			if(a1[i]==a2[i+1] or (i>0 and a1[i]==a2[i-1])):
				count+=int(a1[i]==a2[i+1]) + int(i>0 and a1[i]==a2[i-1])
			if(a2[i]==a1[i+1] or (i>0 and a2[i]==a1[i-1])):
				count+=int(a2[i]==a1[i+1]) + int(i>0 and a2[i]==a1[i-1])
			if(count<(int(a1[i]==a1[i+1]) + int(a2[i]==a2[i+1])+ int(i>0 and a1[i]==a1[i-1])+ int (i>0 and a2[i]==a2[i-1]) )):
				aux=a1[i]
				a1[i]=a2[i]			
				a2[i]=aux

	
	
	l=a1+a2[::-1]
	for i in range(1,n):
		if(l[i]==l[i-1]):
			result+=1	
			
	return result
			
t=1
t=int(input())
for i in range(t):
	print(solve())
	
