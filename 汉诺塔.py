N, M = map(int, input().split())
A = [i for i in range(1, N+1)][::-1]
B = []
C = []

def contains(a, c):
    if a == 'A' and c == 'C':
        temp = A.pop()
        C.append(temp)
        return temp
    elif a == 'A' and c == 'B':
        temp = A.pop()
        B.append(temp)
        return temp
    elif a == 'B' and c == 'C':
        temp = B.pop()
        C.append(temp)
        return temp
    elif a == 'B' and c == 'A':
        temp = B.pop()
        A.append(temp)
        return temp
    elif a == 'C' and c == 'B':
        temp = C.pop()
        B.append(temp)
        return temp
    elif a == 'C' and c == 'A':
        temp = C.pop()
        A.append(temp)
        return temp

def hannoi(n, a, b, c):
    if n == 1:
        no = contains(a, c)
        li.append(f'#{no}: {a}->{c}')
        return
    hannoi(n-1, a, c, b)
    hannoi(1, a, b, c)
    hannoi(n-1, b, a, c)

li = []
hannoi(N, 'A', 'B', 'C')
print(li[M - 1])
print(len(li))
