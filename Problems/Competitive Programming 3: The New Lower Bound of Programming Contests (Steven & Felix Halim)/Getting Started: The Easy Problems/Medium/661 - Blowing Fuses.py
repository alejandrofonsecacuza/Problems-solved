

t=0
while(True):
    if(t!=0):
        print()
    t+=1
    n,m,c=map(int,input().split())
    if(n==0 and m==0 and c==0):
        break
    value=[-1]
    state=[False]*(n+n)
    consumo_total=0
    consumo_maximo=0
    for i in range(0,n):
        value.append(int(input()))
    band=False
    for _ in range(m):
        ind=int(input())
        if(state[ind]):
            state[ind]=False
            consumo_total-=value[ind]
        else:
            state[ind]=True
            consumo_total+=value[ind]
        consumo_maximo=max(consumo_maximo,consumo_total)
 
    print(f"Sequence {t}")
    if(consumo_maximo>c):
        print("Fuse was blown.")
    else:
        print("Fuse was not blown.")
        print(f"Maximal power consumption was {consumo_maximo} amperes.")


