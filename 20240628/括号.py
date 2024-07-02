s = input()
a, b = 0, 0
for i in s:
    if i == '(': a += 1
    else: b += 1
if abs(a - b) != 2:
    ans = 0
elif b > a: # ）多了，需要改成（
    stack = []
    ans = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else: # == ')'
            if len(stack) >= 0:
                ans += 1
            if len(stack):
                stack.pop()
            else: break
else: # （ 多了，需要改成 ）
    stack = []
    ans = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ')':
            stack.append(')')
        else: # == '('
            if len(stack) >= 0:
                ans += 1
            if len(stack):
                stack.pop()
            else: break
print(ans)