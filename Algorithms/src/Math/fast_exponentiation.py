def fast_exponentiation(a, b):
	if b == 0: return 1
	s = fast_exponentiation(a, b//2)
	if b%2 == 0: return s*s
	else: return s*s*a

MOD=(10**9)+7

def fast_exponentiation(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b = b // 2
    return result