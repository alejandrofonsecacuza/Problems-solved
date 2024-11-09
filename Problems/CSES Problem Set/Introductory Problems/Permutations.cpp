#include "bits/stdc++.h"
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
 
 
using namespace std;
typedef vector<int> vi;
typedef long long ll;
 
void solve(){
    int n;cin>>n;
    if(n==1){cout<<1<<"\n";return;}
    if(n<=3 and n>=2){cout<<"NO SOLUTION"<<"\n";return;}
    if(n==4){cout<<"3 1 4 2"<<"\n";return;}
    for(int i=1;i<=n;i+=2)
        cout<<i<<" ";
    for(int i=2;i<=n;i+=2)
        cout<<i<<" ";
    cout<<"\n";
}
 
int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T = 1;
    while(T--)
        solve();
    return 0;
}
 
