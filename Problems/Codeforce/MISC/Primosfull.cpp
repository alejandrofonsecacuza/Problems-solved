#include <bits/stdc++.h>
using namespace std;

bool is_full_prim(int number);
bool is_full_prim2(int number);
typedef vector<pair<int,int>> VII;
int main()

{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
		
	int t,x,y;
	VII vec;
	
	cin>>t;
	while(t--){
		cin>>x>>y;
		vec.push_back(make_pair(x,y));
	}
	
for (auto v :vec){
int c=0;
for (int i=v.first;i<v.second;i++)
{
	if(is_full_prim(i))
	{	
		c++;
	}
}
cout<<c<<endl;
}


  return 0;
}


bool is_full_prim(int number){
	string str_number=to_string(number);
	string sub_str;
	for(auto l: str_number){
		sub_str+=l;
		number=stoi(sub_str);
	for (int i=1;i<=sqrt(number);i++){
		if(number%i==0 and i!=1){
			return false;
		}
	
	}
}
	return true;
}
