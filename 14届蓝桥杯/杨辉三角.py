"""
找一个数出现第一次在第几行
"""
n = int(input())
li = []
li_sort = []
print('[1]')
li_sort.append(1)
while n not in li:
    arr = li.copy()
    li = []
    li.append(1)
    for i in range(len(arr)-1):
        li.append(arr[i] + arr[i+1])
    li.append(1)
    li_sort.extend(li)
    print(li)

if n == 1:
    print(1)
else:
    print(len(li))