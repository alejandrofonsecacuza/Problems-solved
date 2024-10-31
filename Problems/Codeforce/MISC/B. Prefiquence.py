
def zp(l):
  first=True
  lo=[]
  c1=0
  c0=0
  for i in l:
    if i=='1':
      if first:
        lo.append(int (i))
        first=False
      if c0!=0:
        lo.append(c0)
        c0=0
      c1+=1
    elif i=='0':
      if first:
        lo.append(int(i))
        first=False
      if c1!=0:
        lo.append(c1)
        c1=0
      c0+=1
  if c0!=0:
    lo.append(c0)
  elif c1!=0:
    lo.append(c1)
  if lo[0]==1:
    lo.pop(0)
    
  return lo
      
      
      
    
  
def solve():
 # print("Respuestas.")
  n,m=map(int,input().split())
  a=input()
  b=input()
 # print(a)
 # print(b)
  #a=list(a)
  #b=list(b)
  za=zp(a)
  zb=zp(b)
#  print(za)
#  print(zb)
  
  
  #Code
  i,j,k=0,0,0
  while(True):
    r=za[i] - zb[j] 
    if r <= 0:
      k+=za[i]
      i+=1
      j+=1
    else:
      k+=zb[j]
      za[i]=r
      j+=2
    if i>=len(za) or j>=len(zb):
      return k
  
    
 
  
  
    
#print(zp('011101001111')) 
#print(zp('10010'))


t=int(input())
while(t):
  print(solve())
  t-=1
  

  