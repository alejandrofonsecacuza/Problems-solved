def gcd(a, b):
	if b == 0: return a
	return gcd(b, a%b)
def mcm(a,b):
	return (a*b)/gcd(a,b)

