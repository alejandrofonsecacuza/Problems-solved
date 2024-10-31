#include <iostream>
#include <algorithm>
#include <vector>
#include <array>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <chrono>
#include <random>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iomanip>
#include <bitset>
#include <cassert>
 
using namespace std;
 
void solve()
{
    int n;
    cin >> n;
    vector<string> g;
    for(int i = 0; i < n; i++)
    {
        string s;
        cin >> s;
        g.push_back(s);
    }
    bool triangle = false;
    for(int i = 0; i < n; i++)
    {
        int cnt = 0;
        for(int j = 0; j < n; j++)
        {
            if(g[i][j] == '1')
            {
                cnt++;
            }
        }
        if(cnt == 1)
        {
            triangle = true;
        }
        else if(cnt > 1)
        {
            break;
        }
    }
    reverse(g.begin(), g.end());
    for(int i = 0; i < n; i++)
    {
        int cnt = 0;
        for(int j = 0; j < n; j++)
        {
            if(g[i][j] == '1')
            {
                cnt++;
            }
        }
        if(cnt == 1)
        {
            triangle = true;
        }
        else if(cnt > 1)
        {
            break;
        }
    }
    if(triangle)
    {
        cout << "TRIANGLE" << endl;
    }
    else
    {
        cout << "SQUARE" << endl;
    }
}
 
int32_t main(){
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
}