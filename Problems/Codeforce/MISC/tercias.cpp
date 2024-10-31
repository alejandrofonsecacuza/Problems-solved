#include <bits/stdc++.h>
using namespace std;
typedef vector<int>vi;


typedef unsigned long long ull;


/*10

20
40
60
120
170
220
290
360
361
2323*/

int tercias(vi vec){
    int a=0;
    int b=1;
    int c=2;

    int c_b;
    int b_a;

    int contador=0;

    int k=1;
    while(k)
    {
        cout<<"a: "<<a<<" b: "<<b<<" c: "<<c<<endl;
        c_b=vec[c]-vec[b];
        b_a=vec[b]-vec[a];

        if(b==vec.size()-2)k--;


        if(c_b==b_a){
        cout<<"(1)  "<<vec[c]<<" - "<<vec[b]<<" = "<<vec[b]<<" - "<<vec[a]<<endl;
            if(b!=vec.size()-2)
                b++;
            if(c!=vec.size()-1)
                c++;



        contador++;
        }
        else if(c_b>b_a){
            if(b!=vec.size()-2)
                b++;
            if(c!=vec.size()-1)
                c++;
        }
        else if(c_b<b_a){
        for(int j=b;j<c;j++){
                c_b=vec[c]-vec[j];
            for(int i=a;i<j;i++){
                if(vec[j]-vec[i]==c_b){
                    contador++;
                    cout<<"(2)  "<<vec[c]<<" - "<<vec[j]<<" = "<<vec[j]<<" - "<<vec[i]<<endl;
                    break;
                }
                /*if(vec[b]-vec[i]<c_b)
                    break;*/
            }
        }

            if(c!=vec.size()-1){
                c++;
            }else{
            b++;
            }
        }



    }


        return contador;
}







int main()

{
//ios_base::sync_with_stdio(0);
//cin.tie(0);
/*
for(int i=1;i<=100;i++){
    cout<<i<<" ";
}
return 0;
*/
ull n;
ull ni;
cin>>n;
cout<<endl;

vi conjunto;
while(n--){
    cin>>ni;
    conjunto.push_back(ni);
}
sort(conjunto.begin(),conjunto.end());
cout<<endl;
cout<<tercias(conjunto)<<endl;




  return 0;
}
