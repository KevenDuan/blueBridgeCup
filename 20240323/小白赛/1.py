import sys
input = sys.stdin.readline
def main():
    for _ in range(int(input())):
        n, x = map(int, input().split())
        a = [0] + list(map(int, input().split()))
        dp = [set() for _ in range(3)] # i格的j心情
        dp[0].add(0)
        dp[1].add(a[1])
        idx = 1
        for i in range(2, n+1):
            idx = (idx + 1) % 3
            if idx == 2:
                l1, l2 = 0, 1
            elif idx == 1:
                l1, l2 = 0, 2
            elif idx == 0:
                l1, l2 = 1, 2

            dp[idx] = set()
            for j in dp[l1]:
                dp[idx].add(j + a[i])
            for j in dp[l2]:
                dp[idx].add(j + a[i])

        if idx == 2:
            l = 1
        elif idx == 1:
            l = 0
        elif idx == 0:
            l = 2
        if x in dp[idx] or x in dp[l]:
            print('Yes')
        else: print('No')

main()
