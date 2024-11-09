#include<iostream>
using namespace std;
void solve(long long n){
    while(n!=1){
        cout<<n<<" ";
        if(n%2==0){
            n=n/2;
        }else{
         n=n*3+1;
        }
    }
    cout<<1;
}
 
 
int main(){
long long n=0;
cin>>   n;
solve(n);
 
}
