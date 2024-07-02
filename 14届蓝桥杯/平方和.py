count = 0
for i in range(1, 2020):
    j = str(i)
    if '2' in j:count += int(j)**2
    elif '0' in j:count += int(j)**2
    elif '1' in j:count += int(j)**2
    elif '9' in j:count += int(j)**2
print(count)
