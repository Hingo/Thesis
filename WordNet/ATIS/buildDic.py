import os
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic as wnic
from itertools import product
from itertools import groupby
from operator import itemgetter
from nltk.stem.lancaster import LancasterStemmer

def uniqifying(seq):			# Takes a set of 'objects' and makes it unique except list
  seen = set()
  seen_add = seen.add
  return [ x for x in seq if x not in seen and not seen_add(x)]

def uniqifying_list(listOfLists):	# Take a list of lists and uniqify it
  unique_data = [list(x) for x in set(tuple(x) for x in listOfLists)]
  return unique_data

def extractEngWords(line):
  line = line.strip()
  return line.split()

def extractTerminals(prog):
  subs = []

  #s = 'PROJECT(AtomicColSet(COL_FARE()), EXTRACT_ROW_MIN_F(COL_FARE(), AtomicRowPredSet(AtomicRowPred(EQ_DEPARTS(CITY(atlanta), ANY(), ANY(), ANY(), ANY()), EQ_ARRIVES(CITY(dallas), ANY(), ANY(), ANY(), ANY())))))'
  s = prog

  flag = False

  shortArray = []

  for c in s:
    if (c.isupper()) or (c == '_'):
      flag = True
      shortArray.append(c)
    else:
      if flag == True:
	temp = ''.join(shortArray)
	subs.append(temp)
	shortArray = []
	flag = False
	continue
      else:
	continue
  
  truncSubs = subs
  for ss in subs:
    #if ss.endswith('S'):
      #print ss + ' hehe'
    if len(ss) == 1:
      truncSubs.remove(ss)
    if ss == 'ANY':
      truncSubs.remove(ss)
    if ss.startswith('_'):
      truncSubs.remove(ss)
  return truncSubs

def compare(w1, w2):		## returns the 
  #lch_threshold = 2.26
  ss1 = wn.synsets(w1)
  ss2 = wn.synsets(w2)
  #return max(ss1.path_similarity(ss2) for (ss1, ss2) in product(s1, s2))
  lis = []
  for s1 in ss1:
    for s2 in ss2:
      try:
	lch = s1.path_similarity(s2)
      except:
	continue
      # The value to compare the LCH to was found empirically.
      # (The value is very application dependent. Experiment!)
      #if lch >= lch_threshold:
      lis.append((w1, w2, lch))
  if(lis == []):
    return (w1, w2, -1)
  toCheckNone = max(lis, key = itemgetter(2))
  if toCheckNone[2] == None:
    return (w1, w2, -1)
  return toCheckNone

actual_terminal_list = ['AIRCRAFT', 'AIRLINES', 'BETWEEN_CITIES', 'BREAKFAST', 'CITY', 'CLASS', 'COL_AIRCRAFT_TYPE', 'COL_AIRLINES', 'COL_ARRIVAL_TIME', 'COL_DEPARTURE_TIME', 'COL_FARE', 'COL_STOPS', 'COL_TRANSPORT', 'DAYNUM', 'EQ_AIRCRAFT_TYPE', 'EQ_AIRLINES', 'EQ_AIRPORT', 'EQ_ARRIVES', 'EQ_CLASS', 'EQ_DEPARTS', 'EQ_FOOD', 'EQ_NON_STOP', 'EQ_STOPS', 'EXTRACT_ROW_MAX', 'EXTRACT_ROW_MAX_T', 'EXTRACT_ROW_MIN', 'EXTRACT_ROW_MIN_F', 'EXTRACT_ROW_MIN_T', 'MATCH_TIME_AROUND', 'MATCH_TIME_GT', 'MATCH_TIME_LT', 'MEAL', 'MONTH', 'NONE', 'PROJECT', 'ROUND_TRIP', 'TIME', 'WEEKDAY']

seed_maps_Dict = {}
seeding_maps = []
fo = open("./giza_0.1_seed_mappings", "r")
seedMapLine = fo.readline()
while(seedMapLine):
  seedMapLine = seedMapLine.rstrip()
  seeding_maps.append(seedMapLine)
  seedMapLine = fo.readline()
fo.close()
for m in seeding_maps:
  seed_maps_Dict[str(m)] = 1

stemming = LancasterStemmer()
stem_delta = 0.95
simi_threshold = 0.79
learnt_epsilon = 0.9
benchMsFO = open("benchmarkSample.txt", "r")
num = 0
while(1):
  engLine = benchMsFO.readline()
  num += 1
  if not engLine:
    break
  print num
  print str(engLine.rstrip())
  words_in_sentence = extractEngWords(engLine)
  wo = []
  for w in words_in_sentence:
    wo.append(w.lower())
  words_in_sentence = wo
  
  prog = benchMsFO.readline()
  prog = prog.rstrip()
  print str(prog)
  terminals_in_program = extractTerminals(prog)				# terminals_in_program is the list of Terminals
  
  maxSimiArrPerWord = []
  maxSimiArrPerTerm = []
  #to_be_added = []
  for t1 in terminals_in_program:
    ####print str(t1) + ' ---- Terminals'				## the terminals are output here
    if not str(t1) in actual_terminal_list:
      continue
    t1File = open("./Terminals/" + str(t1), "a+")
    dict_words_probs = []
    l1 = t1File.readline()
    if not (l1):
      t1File.close()
      continue
    while(l1):
      l1 = l1.rstrip()
      l1 = l1.lower()
      dict_words_probs.append(l1.split())
      l1 = t1File.readline()
    
    stem_words_prob = []
    #print 'dict_words_probs: ' + str(dict_words_probs)
    for w2 in dict_words_probs:
      word_wo_prob = str(stemming.stem(w2[0]))
      stem_words_prob.append([word_wo_prob, w2[1]])
    stem_words_prob = uniqifying_list(stem_words_prob)
    
    maxSimiArrPerWord = []
    val = ['crap', 'crap', 0]
    for w1 in words_in_sentence:
      ####print str(w1) + ' -------word from sentence'
      #if w1 in dict_words_probs:
	#continue
      #if str(t1) == 'CONTAINS':
	#print w1 + ' - word in sentence from CONTAINS terminal &&&&&&&&&&&&&&&&&&&&'
      val = [w1, w1, 0]
      for w2_prob in stem_words_prob:
	if (str(stemming.stem(w1)) == w2_prob[0]):
	  val = [w1, 'stemming', float(w2_prob[1]) * stem_delta]
	  break
      if not (val[2] == 0):
	maxSimiArrPerWord.append(val)
	#to_be_added.append(val)
	continue
      check_with_all = []
      for w2 in dict_words_probs:
	####print w2
	tempval = compare(w1, w2[0])
	if tempval[2] > 0:
	  check_with_all.append((tempval[0], tempval[1], tempval[2] * float(w2[1]) * learnt_epsilon))
      
      #if not check_with_all == []:
	#for val_as_tuple in check_with_all:
	  #if not (val_as_tuple[2] == 0):
	    #val = [val_as_tuple[0], val_as_tuple[1], val_as_tuple[2]]
	    #if float(val[2]) > simi_threshold:
	      #maxSimiArrPerWord.append(val)
    
      if not check_with_all == []:
	val_as_tuple = max(check_with_all, key = itemgetter(2))
	val = [val_as_tuple[0], val_as_tuple[1], val_as_tuple[2]]
	####print str(tempval) + ' ******************** Map of word to word and similarity val'
      if not (val[2] == 0):
	maxSimiArrPerWord.append(val)
    #if not (maxSimiArrPerWord == []):
      #wToAddToTerm = max(maxSimiArrPerWord, key = itemgetter(2))
      #t1File.write(str(wToAddToTerm[0]) + '\n')
    
    t1File.close()
    
        
    #print "maxSimiArrPerWord: " + str(maxSimiArrPerWord)
    if not (maxSimiArrPerWord == []):
      #for wToAddToTerm in maxSimiArrPerWord:
	#if wToAddToTerm[2] > simi_threshold:
	  #maxSimiArrPerTerm.append([wToAddToTerm[0], t1, wToAddToTerm[2]])
      wToAddToTerm = max(maxSimiArrPerWord, key = itemgetter(2))
      #if str(t1) == 'CONTAINS':
	#print str(wToAddToTerm) + ' - to be added if above simi_threshold from CONTAINS terminal &&&&&&&&&&'
      if wToAddToTerm[2] > simi_threshold:
	maxSimiArrPerTerm.append([wToAddToTerm[0], t1, wToAddToTerm[2]])
      #####print str(maxSimiArrPerWord) + ' ** ' + str(maxSimiArrPerTerm)
  
  
  #-------Options for Additions------------
  
  ##print 'options for additions -##**##- ' + str(maxSimiArrPerTerm)
  
  #-------------------
  
  
  #sameWords = [max(items) for key, items in groupby(maxSimiArrPerTerm, key = itemgetter(0))]
  
  #------------ Sorted by terminals first-------------------
  #sorted_by_second_and_third = list(reversed(sorted(sorted(maxSimiArrPerTerm, key=lambda(e): e[2]), key=lambda(e): e[1])))
  #first_dup_removed = [group.next() for key, group in groupby(sorted_by_second_and_third, key=lambda(e): e[0])]
  
  #sorted_by_first_and_third = list(reversed(sorted(sorted(first_dup_removed, key=lambda(e): e[2]), key=lambda(e): e[0])))
  #sameWords = [group.next() for key, group in groupby(sorted_by_first_and_third, key=lambda(e): e[1])]
  
  #-------------Sorted by words first------------------------
  sorted_by_first_and_third = list(reversed(sorted(sorted(maxSimiArrPerTerm, key=lambda(e): e[2]), key=lambda(e): e[0])))
  first_dup_removed = [group.next() for key, group in groupby(sorted_by_first_and_third, key=lambda(e): e[0])]
  
  sorted_by_second_and_third = list(reversed(sorted(sorted(first_dup_removed, key=lambda(e): e[2]), key=lambda(e): e[1])))
  sameWords = [group.next() for key, group in groupby(sorted_by_second_and_third, key=lambda(e): e[1])]
  
  
  print 'actual additions -**##**- ' + str(sameWords) + '\n'
  for addingHighProb in sameWords:
    termFile = open("./Terminals/" + str(addingHighProb[1]), "a+")
    map_format = str(addingHighProb[1]) + '$' + str(addingHighProb[0])
    if map_format in seed_maps_Dict:
      seed_maps_Dict[map_format] += 1
    else:
      seed_maps_Dict[map_format] = 1
    dict_words_probs = []
    l1 = termFile.readline()
    while(l1):
      l1 = l1.rstrip()
      l1 = l1.lower()
      dict_words_probs.append(l1.split())
      l1 = termFile.readline()
    
    #print 'dict_words_probs: ' + str(dict_words_probs) + ' -------- the dict_words_probs list i.e. Terminal words'
    #print 'addingHighProb: ' + str(addingHighProb)
    
    flag_to_write = 1
    for each_add_word_prob_term in dict_words_probs:
      if str(addingHighProb[0]) == str(each_add_word_prob_term[0]):
	flag_to_write = 0
    if flag_to_write:
      termFile.write(str(addingHighProb[0]) + ' ' + str(addingHighProb[2]) + '\n')
    termFile.close()
  
  blankLine = benchMsFO.readline()

fo = open("giza_map_frequency_0.1_0.79", "w")
for keys, values in seed_maps_Dict.iteritems():
  fo.write(str(keys) + '\t\t' + str(values) + '\n')
fo.close()