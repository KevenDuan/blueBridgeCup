import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, k = map(int, input().split())
row = {}; clum = {}
def tag(r, c):
    if r not in row: row[r] = 1
    if c not in row: row[c] = 1
    
for _ in range(k):
    r, c = map(int, input().split())
    tag(r, c); tag(c, r)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i not in row and j not in clum:
            