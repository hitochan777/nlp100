lines = open("hightemp.txt").readlines()
out1 = open("col1.txt","w") 
out2 = open("col2.txt","w")
for line in lines:
    elems = line.split()
    print(elems)
    out1.write(elems[0]+"\n")
    out2.write(elems[1]+"\n")

out1.close()
out2.close()
