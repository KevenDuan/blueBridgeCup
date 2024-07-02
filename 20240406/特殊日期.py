from datetime import datetime
from datetime import timedelta
d_sta = datetime(1900, 1, 1)
d_end = datetime(9999, 12, 31)
deta = timedelta(days=1)

cnt = 0
while d_sta != d_end:
    y, m_d = list(map(int, str(d_sta.year))), list(map(int, str(d_sta.month) + str(d_sta.day)))
    if sum(y) == sum(m_d):
        cnt += 1
    d_sta += deta
print(cnt)