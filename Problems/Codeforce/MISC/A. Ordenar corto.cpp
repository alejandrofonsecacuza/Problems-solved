#include <bits/stdc++.h>

using namespace std;

int main()

{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	
	int n;
	cin>>n;
	
	
	vector<string> vs;
	while(n--){
		string a;
		cin>>a;
		vs.push_back(a);
	}
	for (auto i :vs){
	
		if(i.size()!=3){
			cout<<"YES"<<endl;
			continue;
			
		}
		 if(i[0]=='b' and i[1]=='c'){
			cout<<"NO"<<endl;
			
		}else if(i[0]=='c' and i[2]=='b'){
				cout<<"NO"<<endl;
		}else{
			cout<<"YES"<<endl;
		}
		
		
	}
}