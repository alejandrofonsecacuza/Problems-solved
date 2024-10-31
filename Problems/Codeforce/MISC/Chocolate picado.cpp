#include <bits/stdc++.h>
using namespace std;

struct corte{
int costo;
int tipo;
corte(int c,int t){
costo=c;
tipo=t;
}

};
typedef vector<corte>vc;
int picar_chocolate(vc vect);

void Burbuja(vc &vect){
    for(int i=0;i<vect.size();i++)
        for(int j=0;j<vect.size()-i-1;j++)
            if(vect[j].costo<vect[j+1].costo){
                swap(vect[j],vect[j+1]);
}
	}


int main()
{
ios_base::sync_with_stdio(0);
cin.tie(0);

int f,c;
cin>>f>>c;
cout<<endl;
vc vect;
int costo;
for(int i=0;i<f-1;i++){
    cin>>costo;
    corte c(costo,0);
    vect.push_back(c);
}
cout<<endl;
for(int i=0;i<c-1;i++){
    cin>>costo;
    corte c(costo,1);
    vect.push_back(c);
}
cout<<endl;
cout<<picar_chocolate(vect)<<endl;;

  return 0;
}

int picar_chocolate(vc v){
int costo_minimo=0;
Burbuja(v);
int l_v=1;
int l_h=1;
while(v.size()){
corte corte_actual=*v.begin();
v.erase(v.begin());
if(corte_actual.tipo){
costo_minimo+=corte_actual.costo*l_v;
l_h++;
}else{
costo_minimo+=corte_actual.costo*l_h;
l_v++;
}
}
return costo_minimo    ;
}
