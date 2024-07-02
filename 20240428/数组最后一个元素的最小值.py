class Solution(object):
    def minEnd(self, n, x):
        ans = list(bin(0|x)[2:])[::-1]
        pre = list(bin(n-1)[2:])[::-1]
        idx = 0
        for i in range(len(ans)):
            if idx >= len(pre): break
            if ans[i] == '0':
                ans[i] = pre[idx]
                idx += 1
        ans.extend(pre[idx:])
        ans.reverse()
        return int(''.join(ans), 2)
        
if __name__ == '__main__':
    s = Solution()
    print(s.minEnd(3, 4))