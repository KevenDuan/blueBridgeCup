def check1(x1, x2, x3): # 四边形情况
    if x1 >= x2 and x1 >= x3:
        if x1 == x2+x3 and li[2]+li[3]-x2 == li[4]+li[5]-x3:
            return True
    if x2 >= x1 and x2 >= x3:
        if x2 == x1+x3 and li[0]+li[1]-x1 == li[4]+li[5]-x3:
            return True
    if x3 >= x1 and x3 >= x2:
        if x3 == x1+x2 and li[0]+li[1]-x1 == li[2]+li[3]-x2:
            return True
    return False

def check2(x1, x2, x3): # 六边形情况
    if x1 >= x2 and x1 > x3:
        if x1 == x2 + x3:
            return True
    if x2 >= x1 and x2 > x3:
        if x2 == x1 + x3:
            return True
    if x3 >= x1 and x3 >= x2:
        if x3 == x1 + x2:
            return True
    return False

T = int(input())
for t in range(T):
    li = [int(t) for t in input().split()]
    ans = 8
    for i in range(0, 2):
        for j in range(2, 4):
            for k in range(4, 6):
                x1, x2, x3 = li[i],li[j],li[k]
                if x1 == x2 and x2 == x3:
                    ans = min(ans, 4)
                if check1(x1, x2, x3):
                    ans = min(ans, 4)
                if x1 == x2 or x2 == x3 or x1 == x3:
                    ans = min(ans, 6)
                if check2(x1, x2, x3):
                    ans = min(ans, 6)
    print(ans)
