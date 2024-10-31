
#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;


//#Orden O(N*K)
int mayor_cantidad_de_diamantes_brute_force(vi v,int k){
int mayor=0;
int suma=0;
for(int i=0;i<(v.size()-(k-1));i++){
    for(int j=i;j<i+k;j++){
        suma=suma+v[j];
    }
    if(suma>mayor){
        mayor=suma;
    }
    suma=0;
}

return  mayor;

}
//#Orden O(k)+O(N-K)=O(n)
int mayor_cantidad_de_diamantes_good(vi v,int k){
int suma=0;
for(int i=0;i<k;i++){
    suma=suma+v[i];
}
int mayor=0;
mayor=suma;
for(int i=1;i<(v.size()-(k-1));i++){
    suma=(suma+v[i+k-1])-v[i-1];
    if(suma>mayor)
        mayor=suma;

}

return  mayor;

}


int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);

vi diamantes;
int n,k;
int ni;
cin>>n;
cout<<endl;
for(int i=0;i<n;i++){
    cin>>ni;
    diamantes.push_back(ni);
}

cout<<endl;
cin>>k;



int a=mayor_cantidad_de_diamantes_good(diamantes,k);

cout<<endl;
cout<<a;



  return 0;
}
