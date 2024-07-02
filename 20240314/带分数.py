from itertools import permutations as pts
n = int(input())
a = '123456789'
ans = 0
for k in pts(a):
    for i in range(1, 8):
        a = int(''.join(k[:i]))
        if a >= n: break
        for j in range(i+1, 9):
            b = int(''.join(k[i:j]))
            c = int(''.join(k[j:]))
            if n * c == a * c + b:
                ans += 1
print(ans)
