def ShowMatriz(n):
	C=""
	C2=""
	for i in range(1,n+1):
		if(i%2):
			C+="##";
			C2+=".."
		else:
			C+="..";
			C2+="##"
	Complete=""
	for i in range(1,n+1):
		if(i%2):
			Complete+=C+"\n"+C+"\n"
		else:
			Complete+=C2+"\n"+C2+"\n"
	print(Complete[0:len(Complete)-1])
t=int(input())
while(t):
	n=int(input())
	ShowMatriz (n)
	t-=1