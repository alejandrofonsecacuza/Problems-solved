#include<iostream>
using namespace std;
const long long mod2=1e9+7;
const long long mod1=1e9+6;
 
 
 
long long fast_powab(long long a, long long b)
{
    if (b == 0) return 1;
    if (b == 1) return a%mod2;
 
    long long result = fast_powab(a, b / 2);
    result = (result * result)%mod2;
 
    if (b % 2 != 0)
    {
        result = (result * a)%mod2;
    }
 
    return result;
}
 
long long fast_powbc(long long a, long long b)
{
    if (b == 0) return 1;
    if (b == 1) return a % mod1;
 
    long long result = fast_powbc(a, b / 2);
    result = (result * result) % mod1;
 
    if (b % 2 != 0)
    {
        result = (result * a) % mod1;
    }
 
    return result;
}
 
 
void solve()
{
    long long a,b,c;
    cin>>a>>b>>c;
    long long aux=fast_powbc(b,c);
    long long result=fast_powab(a,aux);
    cout<<result<<"\n";
}
 
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        solve();
    }
    return 0;
}
