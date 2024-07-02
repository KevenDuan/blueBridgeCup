A, B, C = map(int, input().split())
N = 21
vis = [[[0] * (N) for i in range(N)] for j in range(N)]
def dfs(a, b, c):
    if vis[a][b][c]: return
    vis[a][b][c] = 1
    dfs(a - min(a, B - b), min(a + b, B), c) # A -> B
    dfs(a - min(a, C - c), b, min(a + c, C)) # A -> C
    dfs(min(a + b, A), b - min(b, A - a), c) # B -> A
    dfs(a, b - min(b, C - c), min(c + b, C)) # B -> C
    dfs(min(a + c, A), b, c - min(c, A - a)) # C -> A
    dfs(a, min(b + c, B), c - min(c, B - b)) # C -> B

dfs(0, 0, C)
ans = []
for c in range(C+1):
    for b in range(B+1):
        if vis[0][b][c]:
            ans.append(c)
print(*ans)
