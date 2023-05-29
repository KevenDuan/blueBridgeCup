y = int(input())
sky = ['geng', 'xin', 'ren', 'gui', 'jia', 'yi', 'bing', 'ding', 'wu', 'ji']
ground = ['shen', 'you', 'xu', 'hai', 'zi', 'chou', 'yin', 'mao', 'chen', 'si', 'wu', 'wei']
string = ''
string += sky[y % 10]
string += ground[y % 12]
print(string)
