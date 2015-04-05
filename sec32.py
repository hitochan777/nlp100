from sec30 import *

verbs = set([morph["base"] for li in lists for morph in li if morph["pos"]=="動詞"])

print(verbs)
