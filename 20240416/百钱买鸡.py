
# for i in range(1, 5+1): print('*' * i)

for x in range(20):
    for y in range(40):
        if x*15 + y*9 + (100-x-y) == 300:
            print(f'公鸡:{x}只，母鸡:{y}只，小鸡:{100-x-y}只。')