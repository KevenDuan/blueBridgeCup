nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
res = 0 

def dfs(nums, temp):
    global res
    if len(temp) == 3:
        if not check(temp, 3):
            return
    elif len(temp) == 6:
        if not check(temp, 6):
            return
    elif len(temp) == 9:
        if not check(temp,9):
            return
    elif len(temp) == 12:
        if not check(temp,12):
            return
        else:
            res += 1
            return
    for i in nums:
        new_nums = nums.copy()
        new_nums.remove(i)
        new_temp = temp + [i]
        dfs(new_nums,new_temp)
        
def check(temp, n):
    if n == 3:
        return temp[0] + temp[1] == temp[2]
    elif n == 6:
        return temp[3] - temp[4] == temp[5]
    elif n == 9:
        return temp[6] * temp[7] == temp[8]
    elif n == 12:
        return temp[11] * temp[10] == temp[9]
dfs(nums, [])
print(res)
