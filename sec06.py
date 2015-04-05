import re
def nGram(s,n=1,word=True):
    if word:
        s = re.findall(r"[\w']+", s)
    return [s[i:i+n] for i in range(0,len(s)-n+1)]

x = "paraparaparadise" 
y = "paragraph"

X = set(nGram(x,n=2,word=False))
Y = set(nGram(y,n=2,word=False))

XunionY = X|Y
XintersectionY = X&Y
XminusY = X - Y
print(XunionY)
print(XintersectionY)
print(XminusY)
print("\"se\" is","" if "se" in XintersectionY else "NOT","in X&Y.")




