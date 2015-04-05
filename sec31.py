from sec30 import *

surface = set([morph["surface"] for li in lists for morph in li if morph["pos"]=="動詞"])

print(surface)
