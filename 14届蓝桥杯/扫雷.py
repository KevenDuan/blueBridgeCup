n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def judge(r, c):
    if arr[r][c] == 9: pass
    else:
        if r == 0:
            if c == 0:
                cnt = 0
                for d in range(r+2):
                    for h in range(c+2):
                       if arr[d][h] == 9:
                           cnt += 1
                arr[r][c] = cnt
            elif c == m-1:
                cnt = 0
                for d in range(r+2):
                    for h in range(c-1, c+1):
                       if arr[d][h] == 9:
                           cnt += 1
                arr[r][c] = cnt
            else:
                cnt = 0
                for d in range(r+2):
                    for h in range(c-1, c+2):
                       if arr[d][h] == 9:
                           cnt += 1
                arr[r][c] = cnt
        elif r == n-1:
            if c == 0:
                cnt = 0
                for d in range(r-1, r+1):
                    for h in range(c+2):
                       if arr[d][h] == 9:
                           cnt += 1
                arr[r][c] = cnt
            elif c == m-1:
                cnt = 0
                for d in range(r-1, r+1):
                    for h in range(c-1, c+1):
                       if arr[d][h] == 9:
                           cnt += 1
                arr[r][c] = cnt
            else:
                cnt = 0
                for d in range(r-1, r+1):
                    for h in range(c-1, c+2):
                       if arr[d][h] == 9:
                           cnt += 1
                arr[r][c] = cnt
        else:
            if c == 0:
                cnt = 0
                for d in range(r-1, r+2):
                    for h in range(c+2):
                       if arr[d][h] == 9:
                           cnt += 1
                arr[r][c] = cnt
            elif c == m-1:
                cnt = 0
                for d in range(r-1, r+2):
                    for h in range(c-1, c+1):
                       if arr[d][h] == 9:
                           cnt += 1
                arr[r][c] = cnt
            else:
                cnt = 0
                for d in range(r-1, r+2):
                    for h in range(c-1, c+2):
                       if arr[d][h] == 9:
                           cnt += 1
                arr[r][c] = cnt
    
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 9
            
for i in range(n):
    for j in range(m):
        judge(i, j)

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
            
