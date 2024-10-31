
  
def MinorBinary(v,n):
  numero = n #el numero que buscamos
  l = 0;
  s=len(v)
  r = s-1;
  Mmenor=-1000000000
  while r > l:
    m = (l + r)//2
    if v[m] > numero:
        r = m-1
    elif v[m] == numero:
        return m
    elif v[m]<numero:
        if v[m]>=Mmenor:
          Mmenor=m
        l = m+1

  if v[l]<=numero and v[l]>=Mmenor:
    Mmenor=l
   
  return Mmenor

def solve():
  R=0
  n=int(input())
  Arturo=list(map(int,input().split()))
  Benito=list(map(int,input().split()))  
  Arturo=sorted(Arturo,reverse=True)
  Benito=sorted(Benito)
  
  
  
  for i in Arturo:
    result=MinorBinary(Benito,i)
    if(result>=0):
      R+=1;
      Benito.pop(result)
    else:
      return R
   return R
      
    


t=int(input())
while(t):
  
  print(solve())
  t-=1


