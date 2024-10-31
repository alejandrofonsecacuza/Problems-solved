
def solve():
  a,b=map(int,input().split())
  if a<=b:
    return a,b
  else:
    return b,a

t=int(input())
while(t):
 # n=int(input())
  a,b=solve()
  print(a,b)
  t-=1