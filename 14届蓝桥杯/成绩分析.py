n = int(input())
li = []
for i in range(n):
    li.append (int (input ()))
print(max(li))
print(min(li))
print ('%.2f' % (sum(li)/n))
