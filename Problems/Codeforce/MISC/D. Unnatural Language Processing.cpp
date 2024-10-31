
#include <bits/stdc++.h>

using namespace std;


//CV CVC

string solve(){


int n;
cin>>n;

string word;

for(int i=0;i<n;i++){
    char x;
    cin>>x;
    word+=x;
}
bool cvc=false;
string s;
for(int i=0;i<n;i++){
        s+=word[i];
        if(cvc){
            s+='.';
            cvc=false;
        }
      if((word[i]=='a' or word[i]=='e') and i<n-2){

        if(word[i+2]=='a' or word[i+2]=='e'){
            s+='.';
        }else{
            cvc=true;
        }

      }


}

return s;
}
int main()

{
vector<string> response;
int t;
cin>>t;
while(t--){

    response.push_back(solve());

}

for (int i=0;i<response.size();i++){
    cout<<response[i]<<endl;
}

}


