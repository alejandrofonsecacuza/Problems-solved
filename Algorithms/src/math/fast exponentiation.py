def fast_pow(a, b):
	if b == 0: return 1
	s = fast_pow(a, b//2)
	if b%2 == 0: return s*s
	else: return s*s*a

MOD=(10**9)+7
def fast_pow_with_module(a, b):
	global MOD
	if b == 0: return 1
	s = fast_pow(a, b//2)
	if b%2 == 0: return (s*s)%MOD
	else: return (s*s*a)%MOD
