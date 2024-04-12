import re

def tachdt(s):
    bt = re.match(r"([+-]?\d*)", s)
    hs = bt.group(1) if bt.group(1) else '1'
    b = s.replace(hs, '') if hs != '1' else s
    if hs == '-' and len(b) > 0 and b[0] in ['+', '-']:
        b = b[1:] if len(b) > 1 else ''
        hs += '1'
    return [hs, b]

def rut_gon_dt(a):
    gop = list(filter(lambda x: x != '', [i.replace(" ", "") for i in re.findall(r'[-+]?\s*\d*[\w^]*', a)]))
    bt = []
    bien = []
    for i in gop:
        if (tachdt(i)[0]=="+" or tachdt(i)[0]=="-") and len(tachdt(i)[0])==1:
            bt.append(tachdt(i))
            bt[-1][0] += "1"
            bien.append(tachdt(i)[1])
        else:
            bt.append(tachdt(i))
            bien.append(tachdt(i)[1])
    loc = list(sorted(set(bien), key=bien.index))
    res = []
    for i in loc:
        r_v = ""
        for j in bt:
            if j[1]==i:
                r_v += j[0]
        if eval(r_v)==1:
            res.append(i)
        elif eval(r_v)==-1:
            res.append(f"-{i}")
        elif eval(r_v)!=0:
            res.append(f"{eval(r_v)}{i}")
    r = ""
    r += res[0]
    for i in range(1, len(res)):
        if "-" not in res[i]:
            r += f"+ {res[i]} "
        else:
            res[i] = res[i].replace("-", "")
            r += f"- {res[i]} "
    return r

def cong_tru_dt(a,b,pheptinh):
    if pheptinh == "-":
        b = b.replace('+', 'temp').replace('-', '+').replace('temp', '-')
        gop = list(filter(lambda x: x != '', [i.replace(" ", "") for i in re.findall(r'[-+]?\s*\d*[\w^]*', a + pheptinh + b)]))
    else:
        gop = list(filter(lambda x: x != '', [i.replace(" ", "") for i in re.findall(r'[-+]?\s*\d*[\w^]*', a + pheptinh + b)]))
    return rut_gon_dt(" ".join(gop))
2x +