
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
    
  return lo

def solve():
  s=input()
  zs=zp(s)
  resta=1
  if zs[0]==1 and len(zs)>=4:
    resta+=1
  elif zs[0]==0 and len(zs)>=3:
    resta+=1
  
  return len(zs)-resta
t=int(input())
while(t):
  print(solve())
  t-=1
   