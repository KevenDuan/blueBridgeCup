n, q = map(int, input().split())
s = [0] + [ord(i)-97 for i in list(input())]
diff = [0] * (n + 5)
for i in range(1, n+1):
    diff[i] = s[i] - s[i-1]

for _ in range(q):
    l, r, d = map(int, input().split())
    diff[l] += d
    diff[r+1] -= d

prex = [0]
for i in range(1, n+1):
    prex.append((prex[i-1] + diff[i])%26)

s = ''
for i in range(1, n+1):
    s += chr(prex[i]+97)
print(s)