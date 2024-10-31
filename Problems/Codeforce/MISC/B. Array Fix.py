

def aux(i):
    a=i//10
    b=i%10
    return (a<=b),a,b;
def solve(l): 
  i=0
  n=len(l)-1 
  while i < n:
    if l[i]>l[i+1]:
      if(l[i]<=10):
        return "NO";
      else:
        t=aux(l[i])
        if(t[0]):
          l.pop(i);
          l.insert(i,t[1])
          l.insert(i+1,t[2])
          i=0
          n=len(l)-1
          continue
        else:
          return "NO"
     
    i+=1       
  return "YES"        
                   
                       
                   
       
t=int(input())
while(t):
    _=int(input())
    l=list(map(int,input().split()))
    print(solve(l))
    t-=1


        
    