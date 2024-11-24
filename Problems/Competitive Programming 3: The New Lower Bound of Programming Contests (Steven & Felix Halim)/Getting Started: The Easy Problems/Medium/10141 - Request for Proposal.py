from collections import namedtuple
propuesta=namedtuple('propuesta',['Nombre','Precio','NumRequisitos'])
t=1
while(True):
    n,p=map(int,input().split())
    if(n==0 and p==0):
        break
    propuestas=[]
    requeriments=[]
    for _ in range(n):
        requeriments.append(input())
    for _ in range(p):
        nombre=input()
        precio,num_requisitos=input().split()
        precio=float(precio)
        num_requisitos=int(num_requisitos)
        for __ in range(num_requisitos):
            ____=input()
        propuestas.append(propuesta(nombre,-1*precio,num_requisitos))
    
    propuestas=sorted(propuestas,key=lambda x:(x[2],x[1]),reverse=True)

    if(t!=1):
        print()
    print(f"RFP #{t}")
    t+=1
    print(propuestas[0].Nombre)
        

