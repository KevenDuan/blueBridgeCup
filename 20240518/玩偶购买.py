for _ in range(int(input())):
    n, x, y, a, b = map(int, input().split())
    cnt, a_cnt, b_cnt = n // y, a // x, b // x
    a_cnt = min(a_cnt, b_cnt - 1)
    
    if cnt == 0 or b_cnt == 0:
        print(-1)
        continue
    
    if cnt >= b_cnt + a_cnt: ans = b_cnt + a_cnt
    else: ans = cnt

    print(ans)