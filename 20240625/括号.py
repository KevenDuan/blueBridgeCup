import sys
def comb(a, b):
    top, down = 1, 1
    for i in range(a, a - b, -1):
        top *= i
    for i in range(1, b + 1):
        down *= i
    return top // down
    
s = list(input())
left, right = 0, 0
for i in range(len(s)):
    if s[i] == '(': left += 1
    else: right += 1
if s[0] == ')' or s[-1] == "(": # 首尾的括号必须翻转
        print(1)
        sys.exit()
    
if left == right:
    print(0) # 刚好可以匹配成功
else:
    if left < right: # 保证left > right
        left, right = right, left
    print(comb(left - 1, right))
