import math
count = 1
n = 1
for i in range(19):
    count = count * 2
    n += count
print(n)
print(count)

# 判断互质
a = math.gcd(count, n)
if a == 1:
    print('已经是互质')
