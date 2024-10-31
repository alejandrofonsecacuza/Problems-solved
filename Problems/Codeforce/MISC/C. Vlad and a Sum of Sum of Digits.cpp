#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
const int MAX = 200'007;

int PreCalculo[MAX];
ll Sum(int n){
	ll suma=0;
	while(n!=0){
		int a=n%10;
		suma+=a;

		n=n/10;
	}
	return suma;
}

void solve() {
int x;
	cin >> x;
	cout<<PreCalculo[x]<<'\n';
		
}
	      
          
 
int main(){
PreCalculo[0] = 0;
	for (int i = 1; i < MAX; i++) {
		PreCalculo[i] = PreCalculo[i - 1] + Sum(i);
	}
	ios::sync_with_stdio(false);
	cin.tie(0);
	int tt; cin >> tt; for (int i = 1; i <= tt; i++) {solve();}
}