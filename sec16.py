import sys
import math

if len(sys.argv)<=1:
    print("usage sec16.py -N [-P]")
    sys.exit()

N = int(sys.argv[1])

if(len(sys.argv)>=3):
    prefix = sys.argv[2]
else:
    prefix = "x"

suffix="aa"

def nextString(s):
    if(s==""):
        return 'a'
    prefix = s[:-1]
    suffix = s[-1:]
    if suffix=='z':
        return prefix+"aa"
    else:
        return prefix + chr(ord(suffix)+1)

with open("hightemp.txt","r") as fin:
    lines = fin.readlines()
    step = len(lines)//N + (len(lines)%N!=0)
    for i in range(0,len(lines),step):
        with open(prefix+suffix,"w") as fout:
            for j in range(i,min(i+step,len(lines))):
                fout.write(lines[j]) 
        suffix = nextString(suffix)

