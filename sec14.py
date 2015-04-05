import sys

if len(sys.argv)<=1:
    print("usage sec14.py -N")
    sys.exit()

N = int(sys.argv[1])
with open("output","w") as fout, open("hightemp.txt","r") as fin:
    for line in fin:
        if N <= 0:
            break
        fout.write(line)
        N-=1
