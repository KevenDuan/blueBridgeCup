n = int(input())
N = 20
x = [0] * (N); y = [0] * (N); z = [0] * (N); w = [0] * (N)
for i in range(n):
    x[i], y[i], z[i], w[i] = map(int, input().split())

def get_distance(idx1, idx2):
    return ((x[idx1] - x[idx2])**2 + (y[idx1] - y[idx2])**2 + (z[idx1] - z[idx2])**2)**0.5

dist = [[0] * (N) for _ in range(N)]
for i in range(n):
    for j in range(n):
        dist[i][j] = get_distance(i, j)

f = [[0x3f3f3f3f] * (N) for _ in range(1<<N)]

for i in range(n):
    f[1<<i][i] = 0

for i in range(1<<n):
    for k in range(n):
        if i>>k&1:
            for j in range(n):
                if i>>j&1:
                    f[i][j] = min(f[i][j], f[i-(1<<j)][k] + dist[k][j] * w[j])
                    
ans = 0x3f3f3f3f
for i in range(n):
    ans = min(ans, f[(1<<n)-1][i])
print("%.2f" % ans)