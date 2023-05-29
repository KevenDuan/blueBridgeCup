def bin_search(li, n):
    left = 0
    right = li[-1]
    while left < right:
        mid = (left + right)//2
        if li[mid] < n: left = mid + 1
        else: right = mid
        print(f'你要找的值在{left}~{right}之间')
        

li = [i for i in range(0, 101)]
n = 5
bin_search(li, n)
    
