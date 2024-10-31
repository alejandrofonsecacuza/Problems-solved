for i in range(int(input())):
	s=n=int(input());
	while(n>>1):
		n=n>>1;
		s+=n;
	print(s)
