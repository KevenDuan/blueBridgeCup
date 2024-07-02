#include <iostream>
using namespace std;
int main()
{
  long long n, cnt = 1, R = 1;
  cin >> n;
  while (n > R){
    R = 3 * R + 1;
    cnt ++;
  }
  cout << cnt;
  return 0;
}