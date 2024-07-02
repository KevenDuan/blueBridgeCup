class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        cnt2 = [0] * 3005 # 存的是num2的数出现次数
        for i in nums2:
            cnt2[i] += 1

        for d in range(-1005, 1005): # 枚举需要加的数
            cnt1 = [0] * 3005
            for i in nums1:
                cnt1[i+d] += 1 # 存的是num1+d出现的次数
                
            flag = True
            for i in range(1005):
                if cnt2[i] == 0: continue
                if cnt2[i] > cnt1[i]:
                    flag = False
                    break
            if flag: return d
            
if __name__ == '__main__':
    nums1 = [7, 2, 6, 8, 7]
    nums2 = [7, 6, 5]
    s = Solution()
    print(s.minimumAddedInteger(nums1, nums2))