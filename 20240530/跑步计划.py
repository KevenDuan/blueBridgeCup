from datetime import date
from datetime import timedelta
deta = timedelta(days=1)
sta = date(2023, 1, 1)
end = date(2024, 1, 1)
ans = 0
while sta != end:
    if sta.weekday() == 0 or '1' in str(sta.month) or '1' in str(sta.day):
        ans += 5
    else: ans += 1
    sta += deta
    
print(ans)