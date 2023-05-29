import os
import sys
n=int(input())
nums=[0]+list(map(int,input().split())) # [0 1, 3, 2, 2]
onecnt=[0 for i in range(n+2)] # [0 1 0 0 0 0]
sum=[0 for i in range(n+1)] # 前缀和 [0 4 6 8 0]
num=[0 for i in range(n+1)] # [0 3 2 2 0]
k=1 # 4
for i in range(1,n+1):
    if nums[i]==1:
        onecnt[k]+=1
        sum[k]+=1
    else:
        sum[k]+=sum[k-1]+nums[i]
        num[k]=nums[i]
        k+=1
res=sum[k-1]+onecnt[k] # 8
ans=n
for i in range(1,k):
    p=num[i]
    for j in range(i+1,k):
        p*=num[j]
        if p>res:
            break
        d=p-sum[j]+sum[i-1]+onecnt[i]
        if d==0:
            ans+=1
        # 前缀和 + 1的个数 >= 前缀积 and 前缀积 - 前缀和 > 0
        elif onecnt[i]+onecnt[j+1]>=d and d>0:
            left=min(d,onecnt[i])
            right=min(d,onecnt[j+1])
            ans+=left+right-d+1         
print(ans)
