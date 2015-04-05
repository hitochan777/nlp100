cnt=0
lists = []
with open("neko.txt.mecab","r") as f:
    li = []
    for line in f:
        if line.startswith("EOS"):
            if len(li)>0:
                lists.append(li)
                li = []
        else:
            elems = line.split("\t")
            infos = elems[1].split(",")
            li.append({"surface":elems[0],"base":infos[6],"pos":infos[0],"pos1":infos[1]})
