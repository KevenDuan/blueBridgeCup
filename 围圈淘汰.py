"""
一群人在编好号码，围在一起。
说一个数，与那个数对应的人淘汰掉，重新编号
然后直到剩下最后一个人，游戏结束
"""
n = int(input('died number:'))
p = [int(i) for i in range(1, 6)] # 1~5人游戏
def game(n, p):
    li = p.copy()
    while len(li) > 1:
        num = n
        while num > len(li):
            num -= len(li)
        del li[num - 1]
    return li[0]

print(game(n, p))