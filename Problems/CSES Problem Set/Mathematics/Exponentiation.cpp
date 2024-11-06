#include <iostream>
using namespace std;
 
const int mod = 1e9 + 7;
 
long long fast_pow(long long a, long long b) {
    if (b == 0) return 1;
    if (b == 1) return a % mod;
 
    long long result = fast_pow(a, b / 2);
    result = (result * result) % mod;
 
    if (b % 2 != 0) {
        result = (result * a) % mod;
    }
 
    return result;
}
 
void solve() {
    long long a, b;
    cin >> a >> b;
    cout << fast_pow(a, b) << endl;
}
 
int main() {
    int t;
    cin >> t; // Número de casos de prueba
    while (t--) {
        solve();
    }
    return 0;
}
