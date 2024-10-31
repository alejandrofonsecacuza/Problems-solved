#include <bits/stdc++.h>
using namespace std;
typedef stack<int>pila;
typedef queue<int>resultados;


struct Pila{
    pila p;
    resultados r;

agrega(){
    int n;
    cin>>n;
    p.push(n);
}

consume(){
if(p.size()>1){
    int num1=p.top();
    p.pop();
    int num2=p.top();
    p.pop();
    p.push(num1+num2);
    }else
    cout<<"ERROR"<<endl;
}
    imprime(){
        r.push(p.top());
    }

    show_result(){
        while(r.size()){
            cout<<r.front()<<endl;
            r.pop();
        }

    }
};


int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);

int n;
cin>>n;
Pila calculadora;
string evento;
while(n--){
    cin>>evento;
    if(evento=="AGREGA"){
        calculadora.agrega();
    }else if(evento=="IMPRIME"){
        calculadora.imprime();
    }else if(evento=="CONSUME"){
        calculadora.consume();
    }
}

calculadora.show_result();





  return 0;
}
