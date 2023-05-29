# binary
def guess():
    print('请你从1～100随机选一个数，回答问题。')
    print('你可以回答yes或者no')
    left = 0
    right = 100
    while True:
        mid = (right + left)//2
        # print(left, right, mid)
        print(f'x >= {mid} ?')
        if input() == 'yes':
            left = mid
        else: right = mid
        if left + 1 == right:
            print(f'你选的数一定是{mid}')
            break

guess()
        
            
