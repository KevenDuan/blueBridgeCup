sum = 0
for i in range(1, 21):
    str = f'{i}只青蛙{i}张嘴{2 * i}只眼睛{4 * i}条腿'
    sum += len(str)
    print(str, sum)
