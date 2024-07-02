li = [1, 2, 3, 5, 8]
for i in li:
    a = 3 * i + 2
    b = 5 * i + 3
    c = 8 * i + 5
    if a not in li: 
        li.append(a)
    if b not in li:
        li.append(b)
    if c not in li:
        li.append(c)
    if len(li) >= 30000:
        break

li.sort()
print(li[2019])
