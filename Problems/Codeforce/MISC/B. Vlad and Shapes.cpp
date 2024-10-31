#include <bits/stdc++.h>
//typedef vector<string> vs;
using namespace std;

void solve(){
 	int n;
    cin >> n;
    vector<string> matriz;
    for(int i = 0; i < n; i++)
    {
        string row;
        cin >> row;
        matriz.push_back(row);
    }
    bool triangle = false;    
	for(int i=0;i<n;i++){
		int C=0;
		for(int j=0;j<n;j++){
			if(matriz[i][j] == '1')
            {
                C++;
            }
            
		}
		if(C==1){
			 triangle = true;
		
		}else if(C>1){
			break;
		}
	}
	reverse(matriz.begin(), matriz.end());
	for(int i=0;i<n;i++){
		int C=0;
		for(int j=0;j<n;j++){
			if(matriz[i][j] == '1')
            {
                C++;
            }
            
		}
		if(C==1){
			 triangle = true;
		
		
		}else if(C>1){
			break;
		}
	}
    if(triangle)
    {
        cout << "TRIANGLE" << endl;
    }
    else
    {
        cout << "SQUARE" << endl;
    }	
}
int main() {

    int t = 0;
    cin >> t;
    while (t--) {
        solve();
    }
}