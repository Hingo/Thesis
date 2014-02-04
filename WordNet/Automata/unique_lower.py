import sys


def uniqifying(seq):
  seen = set()
  seen_add = seen.add
  return [ x for x in seq if x not in seen and not seen_add(x)]


nameFile = (sys.argv)[1]

wordL = []
fo = open(nameFile, "r")
line = fo.readline()
while(line):
  line = line.rstrip()
  wordL.append(line.lower())
  line = fo.readline()
fo.close()

i = 1
if(wordL == []):
  print 'No words in file: ' + str(nameFile)
  print 'Total files yet: ' + str(i)
  i = i + 1
else:
  uniqL = uniqifying(wordL)
  fo = open(nameFile, "w")
  for w in uniqL:
    fo.write(str(w) + '\n')
  fo.close()


#manFile = "manual_all_mappings"
#autoFile = "automated_all_mappings"
#manMINUSauto = "manual_MINUS_automated"
#autoMINUSman = "automated_MINUS_manual"

#manList = []
#fo = open(manFile, "r")
#line = fo.readline()
#while(line):
  #line = line.rstrip()
  #manList.append(line.lower())
  #line = fo.readline()
#fo.close()

#autoList = []
#fo = open(autoFile, "r")
#line = fo.readline()
#while(line):
  #line = line.rstrip()
  #autoList.append(line.lower())
  #line = fo.readline()
#fo.close()

#manual_MINUS_automatedList = []
#fo = open(manMINUSauto, "r")
#line = fo.readline()
#while(line):
  #line = line.rstrip()
  #manual_MINUS_automatedList.append(line.lower())
  #line = fo.readline()
#fo.close()

#automated_MINUS_manualList = []
#fo = open(autoMINUSman, "r")
#line = fo.readline()
#while(line):
  #line = line.rstrip()
  #automated_MINUS_manualList.append(line.lower())
  #line = fo.readline()
#fo.close()

#uniqueAutoList = uniqifying(autoList)
#uniqueManList = uniqifying(manList)
#unique_automated_MINUS_manualList = uniqifying(automated_MINUS_manualList)
#unique_manual_MINUS_automatedList = uniqifying(manual_MINUS_automatedList)

#DMminusDW = [item for item in uniqueManList if item not in uniqueAutoList]

#DWminusDM = [item for item in uniqueAutoList if item not in uniqueManList]

#f1o = open("lower_manual_all_mappings", "a+")
#for maps in uniqueManList:
    #f1o.write(str(maps) + '\n')
#f1o.close()

#f2o = open("lower_automated_all_mappings", "a+")
#for maps in uniqueAutoList:
    #f2o.write(str(maps) + '\n')
#f2o.close()

#f3o = open("generatedListFrom_manual_MINUS_automated", "a+")	# the list generated here is made from subtraction of unique lists made after extracting the lists from manual and auto files
#for maps in DMminusDW:
    #f3o.write(str(maps) + '\n')
#f3o.close()

#f4o = open("generatedListFrom_automated_MINUS_manual", "a+")	# the list generated here is made from subtraction of unique lists made after extracting the lists from manual and auto files
#for maps in DWminusDM:
    #f4o.write(str(maps) + '\n')
#f4o.close()


#print 'Manual List: ' + str(len(uniqueManList))
#print 'WordNet List: ' + str(len(uniqueAutoList))
#print 'Manual - WordNet: ' + str(len(unique_manual_MINUS_automatedList))
#print 'WordNet - Manual: ' + str(len(unique_automated_MINUS_manualList))
#print 'Manual - WordNet(generated List From Manual & Automated Files): ' + str(len(DMminusDW))
#print 'WordNet - Manual(generated List From Manual & Automated Files): ' + str(len(DWminusDM))