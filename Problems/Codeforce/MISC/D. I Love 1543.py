from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))
def move(p,d,l):
	f,c=p
	n,m=d
	n-=1+(l*2)
	m-=1+(l*2)
	f-=l
	c-=l
	if(f==0 and c!=m):
   		return (0+l,(c+1)+l)
	elif(c==m and f!=n):
		return ((f+1)+l,c+l)
	elif(f==n and c!=0):
		return ((f+l),(c-1)+l)
	elif(c==0 and f!=0):
		return ((f-1)+l,c+l)
def get_level(p,d):
	n,m=d
	i,j=p
	return min(i,n-1-i,j,m-1-j)

	
	

def find(l,elem):
	response=[]
	for index,value in enumerate(l):
		if(value==elem):
			response.append(index)
	return response
	
def solve():
	n,m=cinline()
	matrix=[]
	u=[]
	for f in range(n):
		i=list(map(int,list(input())))
		response=find(i,1)
		if(response):
			for j in response:
				u.append((f,j))
		matrix.append(i)
	result=0
#	print(u)
	for q in u:
	#	print("q",q)
		l=get_level(q,(n,m))
#		print("level",l)
		aux=q
		p=[aux]
		for i in range(3):
			aux=move(aux,(n,m),l)
			p.append(aux)
		
		path=[]
		for f,c in p:
			path.append(matrix[f][c])
		#print(path)
		if(path==[1,5,4,3]):
			result+=1
	return result
	
	
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
