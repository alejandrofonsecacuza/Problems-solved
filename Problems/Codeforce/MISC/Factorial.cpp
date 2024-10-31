#include <bits/stdc++.h>
using namespace std;
#define ll long long


ll factorial(ll n){
    if(n<=1)return 1;
    return n*factorial(n-1);



}
int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);

cout<<factorial(35);


  return 0;
}
