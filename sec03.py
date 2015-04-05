from operator import itemgetter
import re 
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = re.findall(r"[\w']+", s)

print(sorted([(len(w),w) for w in words], key=itemgetter(0), reverse=True))
