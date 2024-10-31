
#O(n)
def EqualFD(s,s2,fg):
	c=0
	for i in range(len(s)):
		if s[i]!=s2[i]:
			c+=1
		if c>fg:
			return False;
	return True;



def solve(palabra):		
	letras_diferentes=set(palabra)
	#Cantidad letras únicas 
	cl_u=len(letras_diferentes)
	#Cantidad letras totales
	cl_m=len(palabra)
	#Listado de divisores
	conjunto_comprobado=set()
	for i in range(1,(cl_m//2)+1):
		if cl_m%i==0 and i>cl_u-2:
			for j in range(0,len(palabra),i):
				sub_string=palabra[j:j+i]
				if (len(set(sub_string))+1<cl_u):
					continue 
				if({sub_string}<=conjunto_comprobado):
					continue
				else :
					conjunto_comprobado.add(sub_string)
				if EqualFD(sub_string*int(cl_m/i),palabra,1):
					return i;
	return cl_m
				
				
t=int(input())
while t:
	_=int(input())
	palabra=input()
	print(solve(palabra))
	t-=1
			
#print(solve("aaaaaaaaaaaaabc"))
	
	




