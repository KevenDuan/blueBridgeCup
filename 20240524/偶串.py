d = {}
a = list(input())
for i in a:
    if i not in d:
        d[i] = 1
    else: d[i] += 1
    
flag = True
for i in d.values():
    if i&1: flag = False
    
if flag: print('YES')
else: print('NO')