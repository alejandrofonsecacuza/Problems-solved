def solve():
  lo=[]
  n=int(input())
  l=list(map(int,input().split()))
  lo.append(l[0]+1)
  i0,i1=1,0
  l.append(0)
    
  
  while(True):
  #  print("*",l[i0],lo[i1])
    r=l[i0]%lo[i1]
   # print("Rem",r)
    s=l[i0-1]-r
    if s<=0:
      s+=lo[i1]
   # print("Bef",l[i0-1])
   # print("Bef-r",s)
    #print("Push",l[i0]+s)
    lo.append(l[i0]+s)
   # print(lo)
    i0+=1
    i1+=1
    if i0>len(l)-1:
      return lo
    
    
    
    
    
    
    
t=int(input())
while(t):
  #print(solve())
  for i in solve():
    print(i)
 # print("-----")
  t-=1