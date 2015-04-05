c1 = open("col1.txt","rU").readlines()
c2 = open("col2.txt","rU").readlines()
filename = "output"
out = open(filename,"w")
for i in range(0,min(len(c1),len(c2))):
    out.write("%s\t%s\n" % (c1[i].rstrip(),c2[i].rstrip()))


