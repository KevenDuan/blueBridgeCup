X = input(); n = len(X)

x_min = list(str(int(''.join(sorted(list(X))))))
while len(x_min) < n: x_min.insert(1, '0')

x_max = list(str(int(''.join(sorted(list(X), reverse=True)))))
while len(x_min) < n: x_min.append('0')
    
x_min = ''.join(x_min)
x_max = ''.join(x_max)

print(x_max, x_min)