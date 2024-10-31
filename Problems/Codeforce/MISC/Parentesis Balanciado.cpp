#include <bits/stdc++.h>
using namespace std;

typedef stack<char>parentesis;
typedef vector<parentesis>vp;
typedef vector<string>vs;



void parentesisBalanciados(vs vect){

for(int i=0;i<vect.size();i++){
    parentesis p;
    bool bandera=true;
    char elemento;
    for(int j=0;j<vect[i].size();j++){
       elemento=vect[i][j];
        if(elemento=='(' or elemento=='[' or elemento=='{')
            p.push(elemento);
        else{
        if(p.empty()or(p.top()=='(' and elemento!=')')or(p.top()=='{' and elemento!='}')or(p.top()=='[' and elemento!=']')){
                bandera=false;
                break;
            }
              p.pop();
        }

    }
        if(!bandera or p.size()){
        cout<<"No"<<endl;
        }else{
        cout<<"Si"<<endl;
        }
}

}
int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);
int n;
vs vect;
string cadena;

cin>>n;
for(int i=0;i<n;i++){
    cin>>cadena;
    vect.push_back(cadena);
}

parentesisBalanciados(vect);


  return 0;
}
