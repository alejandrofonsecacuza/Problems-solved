#include <bits/stdc++.h>
using namespace std;

struct evento{
char tipo;
int numero_fila;
string nombre;
entrar(){
cin>>tipo;
if(tipo=='E'){
    cin>>numero_fila>>nombre;
}else if(tipo=='A'){
    cin>>numero_fila;
}else{
cout<<"ERROr DE ENTRADA"<<endl;
}
}
};
typedef stack<evento>fila_2;
typedef queue<evento>fila_1;
typedef queue<string>salidas;









int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);
int cantidad_eventos=0;
cin>>cantidad_eventos;
cout<<endl;

fila_1 f1;//cola
fila_2 f2;//pila
salidas f3;//cola

while(cantidad_eventos--){
evento new_evento;
new_evento.entrar();
if(new_evento.tipo=='E'){
    if(new_evento.numero_fila==1)
        f1.push(new_evento);
    else if(new_evento.numero_fila==2)
        f2.push(new_evento);
}else if (new_evento.tipo=='A'){
    if(new_evento.numero_fila==1){
        if(f1.size()){
            f3.push(f1.front().nombre);
            f1.pop();
        }else{
            cout<<"NO AHI NADIE EN LA  FILA 1"<<endl;
        }
    }else if(new_evento.numero_fila==2){
        if(f2.size()){
         f3.push(f2.top().nombre);
            f2.pop();
               }else
            cout<<"NO AHI NADIE EN LA FILA  2"<<endl;
    }
}else{
cout<<"ERROR EN ENTRADA"<<endl;


return 0;
}
cout<<endl;







}
while(f3.size()){
    cout<<f3.front()<<endl;
    f3.pop();
}
  return 0;
}
