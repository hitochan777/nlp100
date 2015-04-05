from operator import itemgetter
import re 
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = re.findall(r"[\w']+", s)
m = {};

indices = [1,5,6,7,8,9,15,16,19]

for i in range(0,len(words)):
    if i+1 in indices:
        m[words[i][:1]] = i+1
    else:
        m[words[i][:2]] = i+1
    
print(m)
