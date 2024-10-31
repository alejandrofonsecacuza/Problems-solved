def MinorBinary(v,n):
  numero = n #el número que buscamos
  encontrado = False
  l = 0;
  s=len(v)
  r = s-1;
  Mmenor=-1000
  while r > l and not encontrado:
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
def BoobleSort(v)

v=[5,19,23,25,31,35,40]
for n in range(0,100):
  print(n,MinorBinary(v,n))