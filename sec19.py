from collections import defaultdict
from operator import itemgetter, attrgetter, methodcaller

freq = defaultdict(int)
with open("hightemp.txt","r") as fin:
    for line in fin:
        name = line.split()[0]
        freq[name] += 1

ans = sorted(freq.items(),key=lambda (k,v):(v,k),reverse=True)

with open("output","w") as fout:
    for li in ans:
        fout.write(li[0]+"\t"+str(li[1])+"\n")


