m, d = map(int, input().split())
str1 = ''
if m == 1: str1 += 'Jan'
elif m == 2: str1 += 'Feb'
elif m == 3: str1 += 'Mar'
elif m == 4: str1 += 'Apr'
elif m == 5: str1 += 'May'
elif m == 6: str1 += 'Jun'
elif m == 7: str1 += 'Jul'
elif m == 8: str1+= 'Aug'
elif m == 9: str1 += 'Sep'
elif m == 10: str1 += 'Oct'
elif m == 11: str1 += 'Nov'
elif m == 12: str1 += 'Dec'

if d < 10: str1 += '0' + str(d)
else: str1 += str(d)

print(str1)
