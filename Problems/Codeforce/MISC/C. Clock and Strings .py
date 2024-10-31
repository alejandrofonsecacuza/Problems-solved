
def solve():
  a,b,c,d=map(int,input().split())
  
  if (c<max(a,b) and c>min(a,b)) and (d>max(a,b) or d<min(a,b)):
    return "YES"
  elif (d<max(a,b) and d>min(a,b)) and (c>max(a,b) or c<min(a,b)):
    return "YES"
  else:
   return "NO"
   

t=int(input())
#t=0
while(t):
#  n=int(input())
  print(solve())
  t-=1
  
#print(solve())
