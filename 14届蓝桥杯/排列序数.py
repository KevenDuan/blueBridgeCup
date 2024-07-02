import itertools
N = input()
n = sorted(list(N))
p = itertools.permutations(n)
cnt = 0
for i in p:
    s = ''
    for j in range(len(i)):
        s += i[j]
        if s[j] != N[j]:
            break
    if s == N:
        print(cnt)
        break
    cnt += 1
