def solve():
	n=input()
	if(n=="1" or n=="4" or n=="78"):
		return "+"
	elif(n[-2:]=="35"):
		return "-"
	elif(n[0]=="9"):
		return 	"*"
	elif(n[:3]=="190"):
		return "?"
t=int(input())
for i in range(t):
	print(solve())
