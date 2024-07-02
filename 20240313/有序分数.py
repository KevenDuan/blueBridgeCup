n = int(input())
ans = [[0, '0/1']]
def check(a, b):
    for i in range(2, a+1):
        if a % i == 0 and b % i == 0: return False
    return True

def dfs(a):
    ans.append([1/a, f'1/{a}'])
    for i in range(2, a):
        if check(i, a):
            ans.append([i/a, f'{i}/{a}'])

for i in range(2, n+1):
    dfs(i)
ans.sort()
ans.append([1, '1/1'])
for i in range(len(ans)):
    print(ans[i][1])
