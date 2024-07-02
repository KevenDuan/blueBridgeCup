n, x = map(int, input().split())
s = sorted(list(input()))
flag = False
for i in range(0, n - x, x):
  if s[i] != s[i + x - 1]:
    flag = True

if flag:
  if s[0] == s[x - 1]:
          print(''.join(s[x - 1:]))
  else:
      print(s[x - 1])
else:
  print(''.join(s[0::x]))