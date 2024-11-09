//Increasing Array
 
#include "bits/stdc++.h"
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
 
 
 
using namespace std;
typedef vector<int> vi;
typedef long long ll;
typedef vector<ll> vl;
 
void solve(){
    int n;
    cin>>n;
    vl v(n);
    for(int i=0;i<n;i++){
        cin>>v[i];
    }
 
 
 
    ll aux=v[0];
    ll response=0;
    for (int i=1;i<n;i++){
        ll res=v[i]-aux;
        if(res<0){
            response+=abs(res);
            v[i]+=abs(res);
        }
        aux=v[i];
 
    }
 
    cout<<response<<"\n";
    return;
}
 
int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T = 1;
    //cin >> T;
    while(T--) {
        solve();
    }
    return 0;
    return 0;
}
