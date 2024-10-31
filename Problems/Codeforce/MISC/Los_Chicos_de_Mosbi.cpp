
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long li;

int dron_mosbi_recursivo(li f,li c){
    static li cant_cuadrados=0;
    if(f<c)
        swap(f,c);
    if(f==c){
        cant_cuadrados++;
        return cant_cuadrados;
    }else{
        f=f-c;
        cant_cuadrados++;
        dron_mosbi_recursivo(f,c);
    }
}

int dron_mosbi_iterativo(li f,li c){
    li cant_cuadrados=0;
    while(f!=c){
    if(f<c)
        swap(f,c);
    f=f-c;
    cant_cuadrados++;
    }
    return ++cant_cuadrados;

}

int dron_mosbi_iterativo_good (li f,li c){
    li cant_cuadrados=0;
    li aux=0;
    while(!c){
    cant_cuadrados=cant_cuadrados+(f/c);
    aux=c;
    c=f%c;
    f=aux;

    }
    return cant_cuadrados;

}
int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);

li f;
li c;
//cin>>f>>c;



int cant_cuadrados=dron_mosbi_iterativo(7,3);
cout<<cant_cuadrados;





  return 0;
}
