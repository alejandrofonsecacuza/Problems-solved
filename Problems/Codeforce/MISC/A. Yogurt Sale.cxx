
#include<iostream>
using namespace std;

int solve(int n,int p,int pr){
	return min(n*p,((n%2)*p)+((n/2)*pr) );
	
	
	}
int main(int argc, char *argv[])
{
 int t,n,p,pr;
 for (int i=0;;i<n){
 cin>>t;}
 while(t--){
 cin>>n>>p>>pr;
 cout<<solve(n,p,pr)<<"\n";	
 	
 	}
}