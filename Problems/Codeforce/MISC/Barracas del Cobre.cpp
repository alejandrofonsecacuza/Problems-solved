#include <bits/stdc++.h>
using namespace std;
typedef long int lli;
typedef vector<lli> vi;







lli mejor_recorrido(vi v,lli k){
    lli mejor_humor=0;
    lli humor_actual=0;

    for(lli i=0;i<k;i++){
            if(i==0)continue;
        humor_actual=humor_actual+(v[i]-v[i-1]);
    }
    mejor_humor=humor_actual;


    for(int i=1;i<v.size()-(k-1);i++){
        humor_actual=humor_actual-(v[i]-v[i-1])-(v[i+(k-2)]-v[i+(k-1)]);
        if(humor_actual>mejor_humor)
            mejor_humor=humor_actual;
    }


    return mejor_humor;



}






int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);

vi espectacularidades;
lli n,k;
lli ni;
cin>>n;
cout<<endl;
for(lli i=0;i<n;i++){
    cin>>ni;
    espectacularidades.push_back(ni);
}

cout<<endl;
cin>>k;



lli mejor_humor=mejor_recorrido(espectacularidades,k);

cout<<endl;
cout<<mejor_humor;

  return 0;
}
