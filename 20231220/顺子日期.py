import datetime
tStart = datetime.datetime(2022, 1, 1)
tEnd = datetime.datetime(2022, 12, 30)
cnt = 0
li = ['012', '123', '234', '345', '456', '567', '678', '789', '890']
while tStart <= tEnd:
    delta = datetime.timedelta(days = 1)
    s = tStart.strftime("%Y%m%d")
    for i in li:
        if i in s:
            cnt += 1
    tStart += delta
print(cnt)
