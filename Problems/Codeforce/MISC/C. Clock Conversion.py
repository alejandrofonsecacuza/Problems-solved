def CastTime(timeToCast):
	h=int(timeToCast[0:2]);
	m=timeToCast[3::]
	if h>=12:
		pos="PM"
	else:
		pos="AM"
	if h==0:
		h=12
	elif h!=12:
		h=h%12
	return str(f"{h if h>=10 else str(0)+str(h)}:{m} {pos}")
#############
t=int(input())
while t:
	hora=input()	
	print(CastTime(hora))
	t-=1