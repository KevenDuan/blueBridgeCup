cous=[0]*(4046)
for i in range(1,2024):
  for j in range(i+1,2024):
    cous[i+j]+=i

print(max(cous))
