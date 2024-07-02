def compare(a,b):
    return a+b > b+a
n=int(input())
num=list(map(str,input().split()))
for i in range(n-1):                   #冒泡排序原理
    for j in range(i+1,n):
        if not compare(num[i],num[j]): #比较拼接后的大小
            num[i],num[j]=num[j],num[i]
for x in num:
    print(x,end='')
