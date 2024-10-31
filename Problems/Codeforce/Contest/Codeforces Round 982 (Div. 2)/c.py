from math import *
def cinint():
	return int(input())
def cinline():
	return list(map(int,input().split()))

def buscar(l,item):
	try:
		return l.index(item)
	except:
		return -1

def solve():
	n=cinint()
	l=cinline()
	s=[]
	for index,value in enumerate(l):
		s.append(value+index)
	response=n
	print(s)
	s.pop()
	while(n in s):
		#s[buscar(s,n)]=-1
		aux=n
		while(True):
			#print("aux",aux)
			i=buscar(s,aux)
			if(aux==n):
				s[i]=-1
			if(i!=-1):
				print("i",i)
				aux+=i+1
			else:
				response=max(aux+i+1,response)
				break
		
	return response
	

t=1
t=int(input())
for i in range(t):
	print(solve())
	
