import sys
sys.setrecursionlimit(1000000)
n=int(input())
f=[0]+list(map(int,input().split()))
vis=[0]*(n+1)#存储崇拜者顺序，1表示第一个小朋友，2表示前一个小朋友崇拜的对象所在的位置下标
global ans
ans=0

def dfs(u,i):
    if vis[u]:#vis[u]访问过
        global ans
        ans=max(ans,i-vis[u])#用当前列表长度i减去已经在T中的那个小朋友的下标
        return
    vis[u]=i#
    dfs(f[u],i+1)#f[u]:寻找下一个崇拜者  i+1:当前构成环的长度+1

for i in range(1,n+1):
    if not vis[i]:
      dfs(i,1)#从i开始遍历，环默认为1

print(ans)
