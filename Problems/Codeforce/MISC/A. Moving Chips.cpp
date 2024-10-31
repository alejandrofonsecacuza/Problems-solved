#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;

bool BloqueCompleto(vi cinta) {
	int n = cinta.size();
	bool Ollo=true;
	bool Uno=false;
	bool Cero=false;
	for(int i=0; i<n; i++) {
		if(cinta[i]==1) {
			Uno=true;
		}
		if(Uno and cinta[i]==0) {
			Cero=true;
		}
		if(Cero and cinta[i]==1) {
			Ollo=false;
		}
	}
	if(Ollo) {
		return true;
	} else {
		return false;
	}

}

int solve() {
	vi cinta;
	int n,ni;
	cin>>n;
	for(int i=0; i<n; i++) {
		cin>>ni;
		cinta.push_back(ni);
	}

	int contador=0;
	while(BloqueCompleto(cinta)==false) {
		bool Uno=false;
		bool Cero=false;
		int IndiceCero=-1;
		reverse(cinta.begin(),cinta.end());
		for(int i=0; i<n; i++) {
			if(cinta[i]==1) {
				Uno=true;

			}
			if(Uno and cinta[i]==0) {
				IndiceCero=n-i-1;
				break;
				
			}
		}

	
		int IndiceUno=-1;
		for(int i=0; i<n; i++) {
			if(cinta[i]==1) {
				IndiceUno=n-i-1;
				break;
			}
		}
		reverse(cinta.begin(),cinta.end());
		swap(cinta[IndiceCero], cinta[IndiceUno]);
		contador++;                               
	}
	return contador;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int tt; cin >> tt; for (int i = 1; i <= tt; i++) {cout<<solve()<<'\n';}
}