from sec30 import *
# morph["pos"]=="名詞" is not needed?
nouns = set([morph["base"] for li in lists for morph in li if morph["pos"]=="名詞" and morph["pos1"]=="サ変接続"])

print(nouns)
