for _ in range(int(input())):
    n, m = map(int, input().split())
    Map = [list(input()) for _ in range(n)]

    def check(tag):
        if Map[0][0] == Map[-1][-1]: return True
        if Map[-1][0] == Map[0][-1]: return True
        if Map[0][0] == Map[0][-1] == tag:
            for i in range(m):
                if Map[-1][i] == tag: return True
        if Map[-1][0] == Map[-1][-1] == tag:
            for i in range(m):
                if Map[0][i] == tag: return True
        if Map[0][0] == Map[-1][0] == tag:
            for i in range(n):
                if Map[i][-1] == tag: return True
        if Map[0][-1] == Map[-1][-1] == tag:
            for i in range(n):
                if Map[i][0] == tag: return True
        return False

    if n == 1 and m == 1:
        print('Yes')
    elif n == 1 and Map[0][0] == Map[0][-1]:
        print('Yes')
    elif m == 1 and Map[0][0] == Map[-1][0]:
        print('Yes')
    elif check('W'):
        print('Yes')
    elif check('B'):
        print('Yes')
    else:
        print('No')