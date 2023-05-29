def build(p, l, r):
    if l == r:
        if s[r] == '1': tree[p] = 'I'
        else: tree[p] = 'B'
        return
    mid = (l + r)//2
    build(2*p, l, mid)
    build(2*p+1, mid+1, r)
    if tree[2*p] == 'I' and tree[2*p+1] == 'I': tree[p] = 'I'
    elif tree[2*p] == 'B' and tree[2*p+1] == 'B': tree[p] = 'B'
    else: tree[p] = 'F'
    
def postorder(p):
    if tree[2*p] != '': postorder(2*p)
    if tree[2*p+1] != '': postorder(2*p+1)
    print(tree[p], end='')

N = int(input())
s = [0] + list(input())
tree = [''] * 4096
build(1, 1, len(s)-1)
postorder(1)
