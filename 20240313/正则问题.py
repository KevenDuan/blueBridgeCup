a = input()
k = 0
def dfs():
    global k
    res = 0
    while k <= len(a) + 1:
        if a[k] == '(':
            k += 1
            res += dfs()
            k += 1
        elif a[k] == 'x':
            k += 1
            res += 1
        elif a[k] == '|':
            k += 1
            res = max(res, dfs())
        elif a[k] == ')':
            break
    return res
print(dfs())
