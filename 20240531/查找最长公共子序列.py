import sys
s = input()
t = input()
for i in range(len(s) - 1, -1, -1): # 枚举长度
    for j in range(0, len(s) - i + 1):
        if t.find(s[j:j + i - 1]) != -1:
            print(s[j:j + i - 1])
            sys.exit()