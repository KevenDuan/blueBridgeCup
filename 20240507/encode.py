def code(c):
    s = list('abcdefghijklmnopqrstuvwxyz')
    p = list('ngzqtcobmuhelkpdawxfyivrsj')
    code = ''
    for i in range(len(c)): 
        idx = s.index(c[i])
        code += p[idx]
    return code

def encode(c):
    s = list('ngzqtcobmuhelkpdawxfyivrsj')
    p = list('abcdefghijklmnopqrstuvwxyz')
    encode = ''
    for i in range(len(c)): 
        idx = s.index(c[i])
        encode += p[idx]
    return encode

code = code('encrypt')
print(code)
encode = encode(code)
print(encode)
