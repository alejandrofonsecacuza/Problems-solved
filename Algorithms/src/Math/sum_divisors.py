
def prime_factorize(n):
	f=2
	factors=defaultdict(int)
	while(n!=1):
		if(n%f==0):
			n//=f
			factors[f]+=1
		else:
			f+=1
	return factors
def factor(n):
	response=[]
	for i in range(1,n+1):
		if(n%i==0):
			response.append(i)
	return response


def sum_divisors(n):
	factors=prime_factorize(n)
	response=1
	
	for key,value in factors.items():
		sum_aux=0
		for exp in range(value+1):
			sum_aux+=(key**exp)
		response*=sum_aux
	return response
	

