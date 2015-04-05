elems = set()
with open("hightemp.txt","r") as fin:
    for line in fin:
        elems.add(line.split()[0])

with open("output","w") as fout:
    for w in elems:
        fout.write(w+"\n")
