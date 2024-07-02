n,m= map(int,input().strip().split())
for i in range(n):
  if m>=9 :
    a=9
  else:
    a=m
  m-=a
  print(a,end="")
