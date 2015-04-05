from sec30 import *

NPs = []

def getNounPhrases(sent):
    p = start = 0
    lis = []
    while p < len(sent):
        if sent[p]["pos"]=="名詞":
            p += 1
        else:
            if p != start:
                s = ""
                for i in range(start,p):
                    s += sent[i]["surface"]
                lis.append(s)
            start = p = p+1
    if p!=start:
        s = ""
        for i in range(start,p):
            s += sent[i]["surface"]
            lis.append(s)
    return lis

for li in lists:
    NPs.extend(getNounPhrases(li))
    
print(set(NPs))
