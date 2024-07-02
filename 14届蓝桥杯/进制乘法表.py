p = int(input())

def Jinzhi(p, i, j):
    li = []
    str1 = ''
    sum = i * j
    while True:
        if sum == 0:
            break
        a = sum # 记录原来的sum
        b = a % p 
        sum = sum // p
        # 判断P进制中有无大于10的数
        if b >= 10:
            b = chr(b + 55)
        li.append(b)
    # 反转输出
    for i in li[::-1]:
       str1 += str(i) 
    return str1 

for i in range(1, p):
    for j in range(1, i+1):
        a = Jinzhi(p, i, j)
        b, c = i, j
        if i >= 10:
            b = chr(i + 55)
        if j >= 10:
            c = chr(j + 55)
        print(f'{b}*{c}={a}',end = ' ')
    print()
