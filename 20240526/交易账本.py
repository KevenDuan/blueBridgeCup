N = 1000 + 10
for _ in range(int(input())):
    n, m = map(int, input().split())
    flag = True # 账本合理性的标记
    outMessge = [[0] * N for _ in range(N)] # 记录交易记录的输出金额
    for id in range(m):
        op = list(map(int, input().split()))
        # 输入部分
        inMoney = 0
        inCount = op[0]
        for i in range(1, 2 * inCount + 1, 2):
            fromId, fromOutNumber = op[i], op[i + 1]
            if fromId > id: # 输入来自于未来的输出不合理
                flag = False
            if fromId != -1:
                inMoney += outMessge[fromId][fromOutNumber]
                outMessge[fromId][fromOutNumber] = 0 # 清空输入中的金额
        # 输出部分 
        outCount = op[2 * inCount + 1]
        outNum, outMoney = 0, 0
        for i in range(2 * inCount + 2, 2 * inCount + 2 * outCount + 2, 2):
            acount, val = op[i], op[i + 1]
            outMessge[id][outNum] += val # 记录输出的信息
            outMoney += val
            outNum += 1
        if fromId != -1 and inMoney != outMoney: # 输出的金额不等于输入的金额
            flag = False
            
    if flag: print('YES')
    else: print('NO')