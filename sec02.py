s1 = "パトカー"
s2 = "タクシー"
s = ""
minlen = min(len(s1),len(s2))

for i in range(0,minlen):
    s += s1[i]
    s += s2[i]

s += s1[minlen:]
s += s2[minlen:]

print(s)
