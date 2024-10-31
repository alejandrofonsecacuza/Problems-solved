#include<iostream>
#include<bitset>
#include <algorithm>
using namespace std;

int Arr[33];
bool esBinario( int num) {
    string numero="";
    numero=to_string(num);
    for (auto i :numero){
    	if(i!='0' and  i!='1'){
    		return false;
    		}
    	}
    	return true;
}
bool divisi(int i=0,int n=10){
		if(esBinario(n))return true;
		if(i>31)return false;
		if(n%Arr[i]==0){
		int r=n/Arr[i];
		return divisi(0,r);
		}
		else{return divisi(i+1,n);}
	}	


int main(int argc, char *argv[])
{

int c=0;
		for(int j=2;j<=100000;j++){
		if(esBinario(j)){
		Arr[c]=j;
		c++;
		}
		}
		int t=0;
		cin>>t;
		int ni;
		while(t--){ 
		cin>ni;
		
		}
	
	
}