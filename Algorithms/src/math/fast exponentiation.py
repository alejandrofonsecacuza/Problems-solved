def fast_pow(a, b):
	if b == 0: return 1
	s = fast_pow(a, b//2)
	if b%2 == 0: return s*s
	else: return s*s*a
