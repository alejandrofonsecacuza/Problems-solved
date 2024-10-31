#include <bits/stdc++.h>

using namespace std;

int main()

{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	

int n,ni,t;

vector<vector<int>>vvi;
cin>>n;




while(n--){
	cin>>t;
	vector<int> vi;
	int menor=100000000;
	while(t--){
	cin>>ni;
	if(ni<menor){
		menor=ni;
	}
	vi.push_back(ni);
	}
	vi.push_back(menor);
	vvi.push_back(vi);
	
}




int aux;
int mul=1;
for(auto i:vvi){
	aux=i[i.size()-1];
	mul=1;
	for(int j=0;j<i.size()-1;j++){
		if(i[j]==aux){
			i[j]=i[j]+1;
			aux=100000000;
		}
		mul*=i[j];
	}
	cout<<mul<<endl;
}

}