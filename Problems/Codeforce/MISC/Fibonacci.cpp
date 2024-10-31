#include <bits/stdc++.h>
using namespace std;
#define print cout<<

int fibonacci(int n){
    if(n==1 or n==0) return 1;
    return fibonacci(n-1)+fibonacci(n-2);
}

int fibonacci_iterativo(int n){
int p1=0;
int p2=1;
int aux=0;
if(n==0 or n==1)return p1;

for(int i=1;i<=n;i++){
    aux=p2;
    p2=p1+p2;
    p1=aux;


}

return p2;
}



int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);

print fibonacci_iterativo(48)<<endl;
print fibonacci(48)<<endl;

  return 0;
}
