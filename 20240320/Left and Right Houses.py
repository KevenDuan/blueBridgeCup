for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input()]    
    b = [0]
    for i in range(n):
        b.append(b[-1] + a[i])
    ans=[]
    for i in range(n+1):
        c=i-b[i]
        d=b[-1]-b[i]
        if c>=i/2 and d>=(n-i)/2:
            ans.append(i)
        
    ans.sort(key=lambda x: abs((n/2)-x))
    print(ans[0])
