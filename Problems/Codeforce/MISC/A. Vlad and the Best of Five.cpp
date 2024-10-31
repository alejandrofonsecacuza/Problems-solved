#include <bits/stdc++.h>

using namespace std;
typedef vector<string>vs;
void solve(vs);
int main()

{
	int t=0;
	cin>>t;
	vs strings;
	string s="";
	while(t--){
		cin>>s;
		strings.push_back(s);
	}
	
	solve(strings);
}

void solve(vs strings){
	for (auto i :strings){
		int A=0;
		int B=0;
		for(auto j:i){
			if(j=='A'){
				A++;
			}else{
				B++;
			}
		}
		if(A>B){
			cout<<"A"<<endl;
		}else{
			cout<<"B"<<endl;
		}
	}
	
}