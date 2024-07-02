#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const ll T = 2e5 + 9;
ll tv[T], a[T];

int main()
{
  ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  ll n, w;cin >> n >> w;
  ll len = 0;
  int flag = 1;
  for(int i = 0; i < T; i++)
  {
    tv[i] = 0;a[i] = 0;
  }
  for(int i = 0; i < n; i++)
  {
    ll s, t, p; cin >> s >> t >> p;
    tv[s] += p;
    tv[t] -= p;
    len = max(len, t);
  }
  for(int i = 0; i < len + 5; i++)
  {
    a[i] = a[i-1] + tv[i];
    if(a[i] > w)
    {
      cout << "No" << endl;
      flag = 0;
      break;
    }
  }
  if(flag)cout << "Yes" << endl;
  return 0;
}