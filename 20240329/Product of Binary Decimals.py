nums = []
for i in range(2,65):
    nums.append(int(str(bin(i))[2:]))

for _ in range(int(input())):
    n = int(input())
    if n in nums or n==1:
        print("YES")
        continue
    flag1 = True
    while n>1:
        flag = True
        for i in range(len(nums)):
            if n%nums[i]==0:
                n = n//nums[i]
                flag = False
        if flag:
            flag1 = False
            break
    if flag1: print("YES")
    else: print("NO")
