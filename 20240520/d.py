# 对于每一位处理
def solve(idx):
    if cnt[idx] % 2 == 0: # 偶数
        return cnt[idx] // 2
    else: # 奇数
        if idx == 0 or idx == 2:
            if cnt[idx+1] % 2 == 0:
                return -1
            else:
                if abs(cnt[idx] - cnt[idx+1]) % 2 == 0:
                    return min(max(cnt[idx], cnt[idx+1]) - abs(cnt[idx] - cnt[idx+1])//2, cnt[idx])
                elif cnt[idx] - cnt[idx+1] == 0: return cnt[idx]
                else: return -1
        else:
            if cnt[idx-1] % 2 == 0:
                return -1
            else:
                if abs(cnt[idx] - cnt[idx-1]) % 2 == 0:
                    return min(max(cnt[idx], cnt[idx-1]) - abs(cnt[idx] - cnt[idx-1])//2, cnt[idx])
                elif cnt[idx] - cnt[idx-1] == 0: return cnt[idx]
                else: return -1
    
for _ in range(int(input())):
    n = int(input())
    a = list(input())
    cnt = [0, 0, 0, 0]
    flag = True
    for i in a:
        if i == 'N': cnt[0] += 1
        elif i == 'S': cnt[1] += 1
        elif i == 'W': cnt[2] += 1
        else: cnt[3] += 1

    c = [0, 0, 0, 0]
    for i in range(4):
        tag = solve(i)
        if tag != -1: c[i] = tag
        else: flag = False
    ans = []
    if cnt[0] == cnt[1] == cnt[2] == cnt[3]:
        c= [0, 0, 0, 0]
        c[0] = c[1] = cnt[0]
        flag = True
    # print(cnt)
    # print(c)
    if flag:
        for i in a:
            if i == 'N':
                if c[0] > 0:
                    ans.append('R')
                    c[0] -= 1
                else:
                    ans.append('H')
            elif i == 'S':
                if c[1] > 0:
                    ans.append('R')
                    c[1] -= 1
                else:
                    ans.append('H')
            elif i == 'W':
                if c[2] > 0:
                    ans.append('R')
                    c[2] -= 1
                else:
                    ans.append('H')
            else:
                if c[3] > 0:
                    ans.append('R')
                    c[3] -= 1
                else:
                    ans.append('H')
        if 'R' in ans and 'H' in ans:
            print(''.join(ans))
        else: print('NO')
    else:
        print('NO')