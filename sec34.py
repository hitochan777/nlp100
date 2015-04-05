from sec30 import *
NPs = set([
		li[i-1]["surface"]+"の"+li[i+1]["surface"] 
		for li in lists
			for i in range(1,len(li)-1)
				if li[i-1]["pos"] == "名詞" and li[i]["surface"]=="の" and li[i+1]["pos"]=="名詞"
				])


print(NPs)
