for _ in range(int(input())):
    B1, B2, B3 = map(int, input().split())
    cntA, cntB = map(int, input().split())
    vA, vB = map(int, input().split())
    if vA > vB: # 确保积木A的体积比B的体积小
        cntA, cntB = cntB, cntA
        vA, vB = vB, vA
    ans = 0
    for i in range(cntA + 1):
        if i * vA > B1:
            break
        for j in range(cntA - i + 1):
            if j * vA > B2:
                break
            
            res = i + j # res存已经放了多少积木数
            remainCntA = cntA - i - j
            remainCntB = cntB
            remain_B1 = B1 - vA * i
            remain_B2 = B2 - vA * j
            remain_B3 = B3
            
            # 将B放入背包1和背包2中
            res += min(remain_B1 // vB, cntB) # 将背包1的剩余空间用B积木尽量装
            remainCntB -= min(remain_B1 // vB, remainCntB)
            res += min(remain_B2 // vB, remainCntB)
            remainCntB -= min(remain_B2 // vB, remainCntB)
        
            # 剩下的背包3先用余下的A装
            res += min(remain_B3 // vA, remainCntA)
            remain_B3 -= min(remain_B3 // vA, remainCntA) * vA
            # 再用B补充余下的背包空间
            res += min(remain_B3 // vB, remainCntB)
            
            ans = max(ans, res)
    print(ans)