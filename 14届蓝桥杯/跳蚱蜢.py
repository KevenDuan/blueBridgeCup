def bfs(s, pos, fuc, d):
    new_pos = (pos + 9 + d) % 9 # 位置
    li = list(s)
    li[pos], li[new_pos] = li[new_pos], li[pos]
    s = ''.join(li)
    if s not in vis:
        vis[s] = 1
        data.append((s, new_pos, fuc + 1))
    
data = [('012345678', 0, 0)]
vis = {'012345678':1}
while data:
    news = data.pop(0)
    if news[0] == '087654321':
        print(news[2])
        break
    bfs(news[0], news[1], news[2], 1)
    bfs(news[0], news[1], news[2], 2)
    bfs(news[0], news[1], news[2], -1)
    bfs(news[0], news[1], news[2], -2)
        
    
