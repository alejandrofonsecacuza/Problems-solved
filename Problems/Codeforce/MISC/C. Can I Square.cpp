
#include <bits/stdc++.h>
#define ll long long
using namespace std;

string f(vector<int>ni);






bool is_square(ll x) {
    ll l = 1, r = 1e9;
    while(l <= r) {
        ll mid = l + (r - l) / 2;
        if(mid * mid == x) return true;
        if(mid * mid > x) r = mid - 1;
        else l = mid + 1;
    }      
    return false;  
}



void solve() {
    ll n; cin >> n;
    ll s = 0;
    for(int i = 0, x; i < n; ++i) {
        cin >> x; s += x;
    }
    if(is_square(s)) cout << "YES\n";
    else cout << "NO\n";
}
int32_t main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int t = 1;
    cin >> t;
    while(t--) {
        solve();
    }
}