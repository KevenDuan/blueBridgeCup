def query(h, l, r):
    return (h[r] - h[l - 1] * pow(p, r - l + 1, mod)) % mod

def judge(s):
    global mod, p
    # owo:6053917
    p = 233
    mod = 10**9 + 7
    n = len(s)
    s = [0] + list(s)
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * p + ord(s[i])) % mod
    
    cnt = 0
    for i in range(1, n - 1):
        if query(h, i, i+2) == 6053917:
            cnt += 1
    return cnt

s, ans = '', 0
for i in range(int(input())):
    t = input()
    res = judge(t) # 计算si的owo数
    
    if i == 0: # 第一次不做任何连接时
        s = t
        ans = res
        print(ans)
        continue
    
    if s[:2] == 'wo' and t[-1] == 'o':
        s = t + s
        ans += res + 1
    elif s[-2:] == 'ow' and t[0] == 'o':
        s = s + t
        ans += res + 1
    elif s[0] == 'o' and t[-2:] == 'ow':
        s = t + s
        ans += res + 1
    elif s[-1] == 'o' and t[:2] == 'wo':
        s = s + t
        ans += res + 1
    else:
        s = s + t
        ans += res
    print(ans)