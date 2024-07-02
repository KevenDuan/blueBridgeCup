def update(G):
    global ans
    dp = [[1] * (h + 1) for _ in range(h + 1)]
    for i in range(h - 2, -1, -1):
        for j in range(h - 2, -1, -1):
            if G[i][j] == G[i + 1][j] == G[i][j + 1]:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + 1
            ans = max(ans, dp[i][j])
            
def turn(G):
    new_G = [[0] * h for _ in range(h)]
    for i in range(h):
        for j in range(h):
            new_G[j][h - i - 1] = G[i][j]
    return new_G

h = int(input())
G = [list(map(int, input().split())) for _ in range(h)]
ans = 0
update(G)
for _ in range(3):
    G = turn(G) # 让G顺时针转90°
    update(G)
print(ans)