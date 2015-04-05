from collections import defaultdict
from operator import itemgetter, attrgetter, methodcaller
from sec30 import *

freq = defaultdict(int)

for li in lists:
    for morph in li:
        freq[morph["surface"]] += 1

ans = sorted(freq.items(), key=lambda t:(t[1],t[0]),reverse=True)

for li in ans:
    print(li[0]+"\t"+str(li[1]))

