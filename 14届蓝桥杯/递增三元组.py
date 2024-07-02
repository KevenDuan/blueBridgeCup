n = int(input())
A = list(map(int, list(input().split())))
B = list(map(int, list(input().split())))
C = list(map(int, list(input().split())))

def check():
    ctime = 0
    for i in range(n):
        a = A[i]
        b = 0
        for j in range(n):
            b = B[j]
            c = 0
            if b <= a: # B数组中不大于A[i]的
                continue
            for k in range(n):
                c = C[k]
                if c > b:
                    ctime += 1
    return ctime

print(check())           
        
