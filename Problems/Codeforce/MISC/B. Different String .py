def solve():
  s=input()
  ul=set(s)
  if len(ul)==1:
    return "NO"
  else:
    j=s[len(s)-1]
    s=j+s
    s=s[:len(s)-1]
    print("YES")
    return s
    
 # print(ul)
t=int(input())
while(t):
  print(solve())
  t-=1