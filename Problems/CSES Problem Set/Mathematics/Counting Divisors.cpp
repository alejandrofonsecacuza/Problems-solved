#include <bits/stdc++.h>
#define nl "\n"
#define nf endl
#define ll long long
#define pb push_back
#define _ << ' ' <<
 
#define INF (ll)1e18
#define mod 998244353
#define maxn 110
using namespace std;
 
 
 
 
bool is_prime(int n)
{
    for (int i=2; i<=sqrt(n); i++)
    {
        if(n%i==0)
        {
            return false;
        }
    }
    return true;
 
}
 
 
map<int,int> descomponer(int n)
{
    map<int,int> factores;
    int factor=2;
 
 
    if(is_prime(n))
    {
        factores[n]++;
        return factores;
 
    }
    while(factor<=n)
    {
 
 
 
        if(n%factor==0)
        {
            factores[factor]++;
            n/=factor;
 
            if(is_prime(n))
            {
                factores[n]++;
                return factores;
 
            }
 
 
        }
        else
        {
            factor++;
        }
    }
    return factores;
 
}
 
 
int solve()
{
    int n;
    cin >> n;
    ll result=1;
    if(n==1)return 1;
 
    for(auto factor:descomponer(n))
    {
 
        result*=(factor.second+1);
 
    }
    return result;
}
int main()
{
 
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t;
    cin >> t; // Número de casos de prueba
    while (t--)
    {
        cout<<solve()<<"\n";
    }
    return 0;
}
