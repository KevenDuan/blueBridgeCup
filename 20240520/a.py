for _ in range(int(input())):
    x, y = map(int, input().split())
    cnt1 = (y + 1) // 2
    if y % 2 != 0:
        rm_x = x - (cnt1-1) * 7 - 11
    else: rm_x = x - cnt1 * 7
        
    cnt2 = 0
    if rm_x > 0:
        cnt2 = (rm_x + 14) // 15
    print(cnt1 + cnt2)