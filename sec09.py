from random import randint
import re
def randomPermutation(s):
    if(len(s)==0):
        return "";
    index = randint(0,len(s)-1)
    return s[index] + randomPermutation(s[0:index]+s[(index+1):])
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = re.findall(r"[\w']+", s)

print([randomPermutation(w[1:len(w)-1]) for w in words])


