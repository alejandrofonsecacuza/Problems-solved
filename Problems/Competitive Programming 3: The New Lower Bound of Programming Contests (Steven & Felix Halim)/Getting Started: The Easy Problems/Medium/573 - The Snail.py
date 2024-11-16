#H is the height of the well in feet 
#U is the distance in feet that the snail can climb during the day, 
#D is the distance in feet that the snail slides down during the night
#F is the fatigue factor expressed as a percentage
while(True):
    H,U,D,F=map(int,input().split())
    if(H==0):
        break
    pos=0
    F=round(F/100,2)
    fatigue=round(F*U,2)
    day=0  
    while(pos<=H and pos>=0):
        day+=1
        pos+=(U if U>0 else 0)     
        if(pos>H):
            break
        pos-=D
        if(pos<0):
            break
        U=round(U-fatigue,2)
    if(pos>=H):
        print(f"success on day {day}")
    else:
        print(f"failure on day {day}")
