def solve(l):
  contador=0
  mayor=-400
  for i in l:
   contador+=i
   if contador<0:
     contador=0
   elif contador>=mayor:
     mayor=contador
  return mayor
   
   
l1=[10,-5,5,1,11,-22,3,7,13]
l2=[-10,-5,5,1,11,-2,3,7]
l3=[10,-5,5,1,11]
  
print(solve(l1))