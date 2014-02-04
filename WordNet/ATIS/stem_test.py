from nltk.stem.lancaster import LancasterStemmer

def uniqifying(seq):
  seen = set()
  seen_add = seen.add
  return [ x for x in seq if x not in seen and not seen_add(x)]

st = LancasterStemmer()

L = ['arrive', 'are', 'driving', 'columns', 'fields', 'whitespace', 'nondigits', 'nonblank', 'nonblanklines']
stL = []
for w in L:
  stL.append(str(st.stem(w)))

#stL = uniqifying(stL)

#print stL
print stL