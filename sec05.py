import re
def nGram(s,n=1,word=True):
    if word:
        s = re.findall(r"[\w']+", s)
    return [s[i:i+n] for i in range(0,len(s)-n+1)]

s = "I am an NLPer"
print(nGram(s,2))
