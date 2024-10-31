def mcd(x,y):
  if(y==0):
    return x
  else:
    return mcd(y,x%y)
    
def solve(n):
  for i in range(1,n):
    if n-mcd(n,i)==i:
      return i;


#print(mcd(27,4))

t=int(input())
while(t):
  n=int(input())
  print(solve(n))
  t-=1
