#include "bits/stdc++.h"
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
 
 
using namespace std;
typedef vector<int> vi;
typedef long long ll;
 
void solve(){
    string s;
    cin>>s;
 
    char a=s[0];
 
    int max_count=0;
    int count_m=0;
    for(const char c:s){
        if(c==a){
            count_m++;
 
        }else{
            max_count=max(max_count,count_m);
            a=c;
            count_m=1;
        }
    }
    max_count=max(max_count,count_m);
 
    cout<<max_count<<"\n";
 
 
 
 
 
 
}
 
int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T = 1;
    //cin >> T;
 
    while(T--) {
        solve();
    }
 
    return 0;
}
