sta = list(input())
end = list(input())
cnt = 0
def turn(idx):
    if sta[idx] == '*':
        sta[idx] = 'o'
        if sta[idx + 1] == '*':
            sta[idx + 1] = 'o'
        else: sta[idx + 1] = '*'
    else:
        sta[idx] = '*'
        if sta[idx + 1] == '*':
            sta[idx + 1] = 'o'
        else: sta[idx + 1] = '*'
    
        
for i in range(len(sta) - 1):
    if sta[i] != end[i]:
        turn(i)
        cnt += 1

print(cnt)
