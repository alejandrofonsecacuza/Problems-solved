#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;


//funcion recursiva para mostrar un vector

void mostrar(vi v){
static int index=0;
if(index==v.size())return;
cout<<v[index++]<<"-";
mostrar(v);
}

void llenar(vi &v,int k){
int aux;

if(k<1)return;
cin>>aux;
v.push_back(aux);
llenar(v,k-1);
}


int main()

{
//ios_base::sync_with_stdio(0);
//cin.tie(0);
vi listado;

llenar(listado,6);
mostrar(listado);



  return 0;
}

