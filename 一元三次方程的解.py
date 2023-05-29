a, b, c, d = map(int, input().split())

def check(x):
    return a * (x**3) + b * (x**2) + c * x + d

i = -100 
while True:
    j = i + 0.001
    if check(i) * check(j) < 0:
        print('%.2f' % ((i + j) / 2),end=' ')
    i = j
    if i >= 100:
        break
