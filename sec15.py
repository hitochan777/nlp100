import sys

if len(sys.argv)<=1:
    print("usage sec15.py -N")
    sys.exit()

N = int(sys.argv[1])
with open("output","w") as fout, open("hightemp.txt","r") as fin:
    lines = fin.readlines()
    for i in xrange(len(lines)-N,len(lines)):
        fout.write(lines[i])
