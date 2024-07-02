#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100010, mod = 99999997;

struct Queue
{
    int h, p; //记录高度、下标
    bool operator< (const Queue &t) const
    {
        return h < t.h;
    }
}a[N], b[N];

int n;
int c[N]; // c[i] 表示b队伍中第i小的数所在的下标
int tr[N]; //树状数组

int lowbit(int x)
{
    return x & -x;
}

void add(int x, int c)
{
    for(int i = x; i <= n; i += lowbit(i)) tr[i] += c;
}

int query(int x)
{
    int res = 0;
    for(int i = x; i; i -= lowbit(i)) res += tr[i];
    return res;
}

int main()
{
    scanf("%d", &n);

    for(int i = 1; i <= n; i++)
    {
        int x;
        scanf("%d", &x);
        a[i] = {x, i};
    }

    for(int i = 1; i <= n; i++)
    {
        int x;
        scanf("%d", &x);
        b[i] = {x, i};
    }

    sort(a + 1, a + 1 + n);
    sort(b + 1, b + 1 + n);

    //下标做映射
    for(int i = 1; i <= n; i++) c[a[i].p] = b[i].p;
    for(int i = 1; i <= n; i++) cout << a[i].p << " ";
    cout << endl;
    for(int i = 1; i <= n; i++) cout << b[i].p << " ";
    cout << endl;
    for(int i = 1; i <= n; i++) cout << c[i] << " ";
    cout << endl;

    //求逆序对数量
    int res = 0;
    for(int i = n; i; i--)
    {
        res = (res + query(c[i])) % mod;
        add(c[i], 1);
    }

    printf("%d\n", res);

    return 0;
}

/*
10
10 1 5 2 7 4 9 3 6 8 
7 5 1 8 10 4 6 2 3 9
*/