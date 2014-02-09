from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic as wnic
from itertools import product
from operator import itemgetter

def compare_ic(w1, w2):
  brown_ic = wnic.ic('ic-brown.dat')
  s1 = wn.synsets(w1)
  s2 = wn.synsets(w2)
  return max(ss1.res_similarity(ss2, brown_ic) for (ss1, ss2) in product(s1, s2))

def compare(w1, w2):		## returns the 
  #lch_threshold = 2.26
  ss1 = wn.synsets(w1)
  ss2 = wn.synsets(w2)
  #return max(ss1.path_similarity(ss2) for (ss1, ss2) in product(s1, s2))
  lis = []
  for s1 in ss1:
    for s2 in ss2:
      ####print str(s1) + ' ' + str(s2) + '\n'
      try:
	lch = s1.path_similarity(s2)
      except:
	continue
      # The value to compare the LCH to was found empirically.
      # (The value is very application dependent. Experiment!)
      #if lch >= lch_threshold:
      lis.append((s1, s2, lch))
      #print '\n' + str((s1, s2, lch)) + '\n'
  if(lis == []):
    return ()
  #print lis
  return max(lis, key = itemgetter(2))

#for w1, w2 in product(['insert', 'after'], ['inserting', 'suffix']):
for w1, w2 in product(['contains', 'mentions', 'occurs', 'present', 'substring'], ['have']):
  print "Path similarity: " + str(compare(w1, w2)) + '\n'

