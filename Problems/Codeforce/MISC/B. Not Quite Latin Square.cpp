
#include <bits/stdc++.h>

using namespace std;

char arr[3][3];
char f();

int main()

{
vector<char>vc;
int t;
cin>>t;


while(t--){
    for(int i=0;i<3;i++){
       for(int j=0;j<3;j++){
         char a;
         cin>>a;
         arr[i][j]=a;


       }
    }
    vc.push_back(f());
}
for(int i=0;i<vc.size();i++){
    cout<<vc[i]<<endl;
}


}

char f(){
    for(int i=0;i<3;i++){
       for(int j=0;j<3;j++){
        if(arr[i][j]=='?'){

            if(j==0){
              if((arr[i][1]=='A' and arr[i][2]=='B')or (arr[i][1]=='B' and arr[i][2]=='A')){
                return 'C';
              }else if((arr[i][1]=='A' and arr[i][2]=='C')or (arr[i][1]=='C' and arr[i][2]=='A')){
                return 'B';
              }else if((arr[i][1]=='B' and arr[i][2]=='C')or (arr[i][1]=='C' and arr[i][2]=='B')){
               return 'A';
              }
            }
            if(j==1){
              if((arr[i][0]=='A' and arr[i][2]=='B')or (arr[i][0]=='B' and arr[i][2]=='A')){
                return 'C';
              }else if((arr[i][0]=='A' and arr[i][2]=='C')or (arr[i][0]=='C' and arr[i][2]=='A')){
                return 'B';
              }else if((arr[i][0]=='B' and arr[i][2]=='C')or (arr[i][0]=='C' and arr[i][2]=='B')){
                return 'A';
              }
            }
                       if(j==2){
              if((arr[i][0]=='A' and arr[i][1]=='B')or (arr[i][0]=='B' and arr[i][1]=='A')){
                return 'C';
              }else if((arr[i][0]=='A' and arr[i][1]=='C')or (arr[i][0]=='C' and arr[i][1]=='A')){
                return 'B';
              }else if((arr[i][0]=='B' and arr[i][1]=='C')or (arr[i][0]=='C' and arr[i][1]=='B')){
             return 'A';
              }
            }






        }
       }
    }
}
