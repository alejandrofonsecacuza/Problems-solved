#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int Quest(vector<int>&ai,vector<int>&bi,int k);
int main()

{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

int t,n,k,a,b,m;

vector<int> response;

	cin>>t;
	while(t--){
	vector<int> ai;
	vector<int> bi;
	cin>>n>>k;
	m=n;
	while(m--){
		cin>>a;
		ai.push_back(a);
	}
	m=n;
	while(m--){
		cin>>b;
		bi.push_back(b);
	}
	response.push_back(Quest(ai,bi,k));
	}



for(int i=0;i<response.size();i++){
	cout<<response[i]<<endl;
}







}

int Quest(vector<int>&ai,vector<int>&bi,int k){
int d=ai.size();
int o=min(k, d);
int movs=0;
int indexai=1;
int mayor=0;
int suma=0;
int mayor_suma=0;


while(indexai<=o){

for(int i=0;i<indexai;i++){
	suma+=ai[i];
	if(bi[i]>mayor){
		mayor=bi[i];
	}
}
movs=k-indexai;
suma+=movs*mayor;
if(suma>mayor_suma){
	mayor_suma=suma;
}

indexai++;
mayor=0;
suma=0;
}

return mayor_suma;
}
