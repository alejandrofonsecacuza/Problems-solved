#include <bits/stdc++.h>
using namespace std;
typedef vector<int>vi;

int destrullendo_edificios(vi v){
vi v_aux=v;
sort(v_aux.begin(),v_aux.end());
int mayor_rectangulo=0;
while(v_aux.size()){
int cantidad_de_edificios=0;
int menor_altura=v_aux[0];
int cantidad_elementos_menores=count(v_aux.begin(),v_aux.end(),menor_altura);
v_aux.erase(v_aux.begin());
vector<int>::iterator index;
if(cantidad_elementos_menores>1){
        int contador_multiplisidades=0;
        for(auto i=v.begin();i!=v.end();i++){
            if(*i==menor_altura){
                contador_multiplisidades++;
            }
            if(contador_multiplisidades==cantidad_elementos_menores){
               index=i;
                break;
            }
        }
}else{
index=find(v.begin(),v.end(),menor_altura);
}
//cout<<endl;
//cout<<"ELEMENTO SEGUIDOS MENORES O IGUAL A EL:"<<*index<<endl;
//cout<<"Mayores o iguales que el a su derecha seguidos:"<<endl;
for(auto i=index;i!=v.end();i++){
    if(menor_altura<=*i){
      //cout<<*i<<"-";
        cantidad_de_edificios++;
    }else
        break;
}
//cout<<endl;
//cout<<"Mayores o iguales que el a su isquierda seguidos :"<<endl;
for(auto j=index;j!=v.begin()-1;j--){
    if(menor_altura<=*j){
       // cout<<*j<<"-";
        cantidad_de_edificios++;
   } else
        break;
}
int resultado=(cantidad_de_edificios-1)*menor_altura;
if(resultado>mayor_rectangulo)
    mayor_rectangulo=resultado;



}
cout<<endl;
return mayor_rectangulo;


}


int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);
int n;cin>>n;
cout<<endl;
int ni;
vi alturas;
while(n--){
cin>>ni;
alturas.push_back(ni);
}
cout<<endl;
cout<<endl;

cout<<destrullendo_edificios(alturas)<<endl;


  return 0;
}
