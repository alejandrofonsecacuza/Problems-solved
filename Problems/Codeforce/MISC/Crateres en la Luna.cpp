#include <bits/stdc++.h>
using namespace std;


//typedef int matriz[][];
int matriz[10][10]=
{{0,0,0,0,0,0,0,0,1,1},
 {0,1,1,1,1,0,0,0,1,1},
 {0,0,0,1,1,0,0,0,0,1},
 {0,0,0,1,1,0,0,0,0,1},
 {0,0,0,0,1,0,0,0,0,0},
 {0,0,0,1,9,0,0,0,0,0},
 {0,1,1,1,0,0,0,0,1,0},
 {0,1,1,0,0,0,0,1,1,0},
 {0,0,0,0,0,0,0,1,1,0},
 {0,0,0,0,0,0,0,0,0,0}
 };





int dfs(int f,int c){
    if(matriz[f][c]==0)return 0;

    if(f<0 or c<0 or f>=10 or c>=10)return 0;

    int cantidad_minerales=matriz[f][c];
    matriz[f][c]=0;

    cantidad_minerales+=dfs(f+1,c);
    cantidad_minerales+=dfs(f-1,c);
    cantidad_minerales+=dfs(f,c+1);
    cantidad_minerales+=dfs(f,c-1);

    return cantidad_minerales;
}

int main()

{
ios_base::sync_with_stdio(0);
cin.tie(0);

int current_crater=1;

int mayor=0;
for(int i=0;i<10;i++){
    for(int j=0;j<10;j++){
        if(matriz[i][j]){
            current_crater++;
            int cantidad_minerales=dfs(i,j);
            if(cantidad_minerales>mayor){
                mayor=cantidad_minerales;
            }

        }



    }

}


cout<<"MAYOR CANTIDAD : "<<mayor;




  return 0;
}
