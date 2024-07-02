#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
bool Map[25][25]; 
ll dp[1<<21][25];
inline int gcd(int a, int b){return b==0 ? a : gcd(b, a%b);}
int main(void)
{
	ll res = 0;
	for(int i = 1;i <= 21; i++){
		for(int j = 1; j <= 21; j++){
		if(gcd(i, j) == 1) Map[i-1][j-1] = Map[j-1][i-1] = true;
		else Map[i-1][j-1] = Map[j-1][i-1] = false;
	    }
	}
	dp[1][0] = 1;
	for(int i = 1; i < (1<<21); i++){
	    for(int j = 0; j < 21; j++){
		    if(!(i>>j&1)) continue;
		    for(int k = 0; k < 21; k++){
			    if((i>>k&1) || !Map[j][k]) continue;
			    dp[i+(1<<k)][k] += dp[i][j];
		    }
	    }
	}
	for(int i = 0; i < 21; i++) 
		res += dp[(1<<21)-1][i];
	cout <<res;
	return 0;
}