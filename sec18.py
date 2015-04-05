from operator import itemgetter, attrgetter, methodcaller
lines = []
with open("hightemp.txt","r") as fin:
    for line in fin:
        elems = line.split()
        elems[2] = float(elems[2])
        lines.append(tuple(elems))

lines.sort(key=itemgetter(2),reverse=False)

with open("output","w") as fout:
     for t in lines:
        fout.write("\t".join(map(str,t))+"\n")
