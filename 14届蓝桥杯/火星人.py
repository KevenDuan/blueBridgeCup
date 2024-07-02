import itertools
n = int(input())
m = int(input())
li = tuple(map(int, input().split()))
li_sort = sorted(li)
p = itertools.permutations(li_sort)
num = 1
a = None
for i in p:
    if i == li:
        a = num
    if a != None: 
      if a + m == num:
        t = i
        break
    num += 1

s = ''
for i in t:
    s += str(i) + ' '
print(s)
