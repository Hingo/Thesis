import sys

def uniqifying(seq):
  seen = set()
  seen_add = seen.add
  return [ x for x in seq if x not in seen and not seen_add(x)]

namefile = (sys.argv)[1]
wordl = []
fo = open(namefile, "r")
line = fo.readline()
while(line):
  line = line.rstrip()
  wordl.append(line.lower())
  line = fo.readline()
fo.close()

i = 1
if(wordl == []):
  print 'no words in file: ' + str(namefile)
  print 'total files yet: ' + str(i)
  i = i + 1
else:
  uniql = uniqifying(wordl)
  fo = open(namefile, "w")
  for w in uniql:
    fo.write(str(w) + '\n')
  fo.close()

#manfile = "manual_all_mappings"
#autofile = "automated_all_mappings"
#manminusauto = "manual_minus_automated"
#autominusman = "automated_minus_manual"
#manlist = []
#fo = open(manfile, "r")
#line = fo.readline()
#while(line):
  #line = line.rstrip()
  #manlist.append(line.lower())
  #line = fo.readline()
#fo.close()
#autolist = []
#fo = open(autofile, "r")
  #autolist.append(line.lower())
#manual_minus_automatedlist = []
#fo = open(manminusauto, "r")
  #manual_minus_automatedlist.append(line.lower())
#automated_minus_manuallist = []
#fo = open(autominusman, "r")
  #automated_minus_manuallist.append(line.lower())
#uniqueautolist = uniqifying(autolist)
#uniquemanlist = uniqifying(manlist)
#unique_automated_minus_manuallist = uniqifying(automated_minus_manuallist)
#unique_manual_minus_automatedlist = uniqifying(manual_minus_automatedlist)
#dmminusdw = [item for item in uniquemanlist if item not in uniqueautolist]
#dwminusdm = [item for item in uniqueautolist if item not in uniquemanlist]
#f1o = open("lower_manual_all_mappings", "a+")
#for maps in uniquemanlist:
    #f1o.write(str(maps) + '\n')
#f1o.close()
#f2o = open("lower_automated_all_mappings", "a+")
#for maps in uniqueautolist:
    #f2o.write(str(maps) + '\n')
#f2o.close()
#f3o = open("generatedlistfrom_manual_minus_automated", "a+")	# the list generated here is made from subtraction of unique lists made after extracting the lists from manual and auto files
#for maps in dmminusdw:
    #f3o.write(str(maps) + '\n')
#f3o.close()
#f4o = open("generatedlistfrom_automated_minus_manual", "a+")	# the list generated here is made from subtraction of unique lists made after extracting the lists from manual and auto files
#for maps in dwminusdm:
    #f4o.write(str(maps) + '\n')
#f4o.close()
#print 'manual list: ' + str(len(uniquemanlist))
#print 'wordnet list: ' + str(len(uniqueautolist))
#print 'manual - wordnet: ' + str(len(unique_manual_minus_automatedlist))
#print 'wordnet - manual: ' + str(len(unique_automated_minus_manuallist))
#print 'manual - wordnet(generated list from manual & automated files): ' + str(len(dmminusdw))
#print 'wordnet - manual(generated list from manual & automated files): ' + str(len(dwminusdm))
