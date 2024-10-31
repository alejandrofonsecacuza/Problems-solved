#include<iostream>
using namespace std;

bool prim(int number,int n){
	if(n==1){
		return true;
	}else{
		if(number%n==0)
		return false;
		else{
			prim(number,n-1);
		}
	}
	
	
}

int main(){
	for(int i=2;i<100;i++){
	cout<<i<<" ";	
	cout<<prim(i,i-1)<<endl;
}
}