import sys
# input = sys.stdin.readline

def uncode(s):
    model = sorted(set(s))
    d = {}
    for i in range(len(model)):
        d[model[i]] = model[-(1+i)]
    ans = []
    for i in s:
        ans.append(d[i])
    print(''.join(ans))

for _ in range(int(input())):
    n = int(input())
    s = input()
    uncode(s)