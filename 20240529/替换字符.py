s = [0] + list(input())
for _ in range(int(input())):
    op = list(input().split())
    sta, end = int(op[0]), int(op[1])
    for i in range(sta, end + 1):
        if s[i] == op[2]: s[i] = op[3]

print(''.join(s[1:]))