#E. Find the Car
import math
def Vel(D,T):
  V=[]
  Arr=list(zip(D,T))
  for i in range(len(Arr)-1):
    V.append(abs(Arr[i][0]-Arr[i+1][0])/abs(Arr[i][1]-Arr[i+1][1]))
  V.append(0)
  return V
  
def MinorBinary(v,n):
  numero = n #el número que buscamos
  l = 0;
  s=len(v)
  r = s-1;
  Mmenor=-1000000000
  while r > l:
    m = (l + r)//2
    if v[m] > numero:
        r = m-1
    elif v[m] == numero:
        return v[m]
    elif v[m]<numero:
        if v[m]>=Mmenor:
          Mmenor=v[m]
        l = m+1

  if v[l]<=numero and v[l]>=Mmenor:
    Mmenor=v[l]
   
  return Mmenor
  
 
  
def solve():
  
  n,k,q=map(int,input().split())
  D=list(map(int,input().split()))
  T=list(map(int,input().split()))
  D.insert(0,0)
  T.insert(0,0)
  V=Vel(D,T)
  
 
  Q=[]
  while(q):
   Q.append(int(input()))
   q=q-1
  Arr = {clave: (valor_b, valor_c) for clave, valor_b, valor_c in zip(D,T,V)}
  
  sum=0
 # print("Resultados:")
  for d in Q:
    sum=0
    
    m=MinorBinary(D,d)
   # print(m)
   # print(Arr[m])
    aux=Arr[m]
    sum=aux[0]
    if aux[1]!=0:
     sum=sum+((d-m)/(aux[1]))
    print(math.floor(sum))
  
  #print("Resultado")
  return


t=int(input())
while(t):
	
	solve()
	t-=1
	
