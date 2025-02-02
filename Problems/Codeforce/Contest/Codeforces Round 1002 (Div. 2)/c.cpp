#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<vector<int>> a(n, vector<int>(n));
    vector<vector<int>> pr(n, vector<int>(n + 1, 0));

    // Read input matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    // Compute prefix sum array
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            pr[i][j + 1] = pr[i][j] + a[i][n - 1 - j];
        }
    }

    int ans = -1;
    int mx = n;

    for (int id = 0; id < mx; id++) {
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (pr[i][id] == id) {
                cnt++;
            }
        }

        if (cnt != 0) {
            ans = id;
        }

        mx = min(mx, id + cnt);
    }

    cout << ans + 1 << "\n";
}

int main() {
    int t=0;
    cin>>t;
    for(int i=0;i<t;i++){
    solve();
    }

    return 0;
}
