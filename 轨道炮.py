N = int(input())
x_list = []
y_list = []
v_list = []
d_list = []
for _ in range(N):
    x, y, v, d = map(str, input().split())
    x_list.append(int(x))
    y_list.append(int(y))
    v_list.append(int(v))
    d_list.append(d)

def get_max(li):
    li_set = set(li)
    mmax = -1
    for i in li_set:
        mmax = max(mmax, li.count(i))
    return mmax

num = -1
for j in range(1001):
    num = max(num, get_max(x_list), get_max(y_list))
    for i in range(len(d_list)):
        if d_list[i] == 'U':
            y_list[i] += v_list[i]
        elif d_list[i] == 'D':
            y_list[i] -= v_list[i]
        elif d_list[i] == 'R':
            x_list[i] += v_list[i]
        elif d_list[i] == 'L':
            x_list[i] -= v_list[i]

print(num)
