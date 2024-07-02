# 请在此输入您的代码
nm= input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))

out = 0 # 合并次数
i = 0 # 索引
while i != len(a): # 结束条件
    while a[i] != b[i]: # 对比直到相等为止
        if (a[i] > b[i]):
            b[i] = b[i]+ b.pop(i+1) # 删掉并且加上第i+1个数
            out+=1
        elif (a[i] < b[i]):
            a[i] = a[i]+ a.pop(i+1)
            out+=1
    i+=1
print(out)