def cipher(s):
    return "".join([substitute(w) for w in s])

def substitute(word):
    if(word.islower()):
        return chr(219-ord(word))
    else:
        return word
