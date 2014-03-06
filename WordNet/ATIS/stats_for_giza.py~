f1o = open("minimal_manual_all_mappings", "r")
manList = []
line = f1o.readline()
while(line):
  line = line.strip()
  manList.append(line)
  line = f1o.readline()
f1o.close()


autoDict = {}
f2o = open("giza_map_frequency_0.1_0.79", "r")
line = f2o.readline()
while(line):
  line = line.rstrip()
  frq = line.split()
  autoDict[str(frq[0])] = frq[1]
  line = f2o.readline()
f2o.close()

#autoDict = {}
#f2o = open("Maps_after_weed2", "r")
#line = f2o.readline()
#while(line):
  #line = line.rstrip()
  #autoDict[str(line)] = -1
  #line = f2o.readline()
#f2o.close()

DMminusDW = {}
for item in manList:
  if item not in autoDict:
    DMminusDW[item] = -1

#DMminusDW = [item for item in manList if item not in autoList]

DWminusDM = {}
for item in autoDict:
  if item not in manList:
    DWminusDM[item] = autoDict[item]

#DWminusDM = [item for item in autoList if item not in manList]

f3o = open("manual-giza_automatedMaps_0.1_0.79", "a+")
for keys, values in DMminusDW.iteritems():
    f3o.write(str(keys) + '\t\t\t' + str(values) + '\n')
f3o.close()

f4o = open("giza_automated_0.1_0.79-manualMaps", "a+")
for keys, values in DWminusDM.iteritems():
    f4o.write(str(keys) + '\t\t\t' + str(values) + '\n')
f4o.close()


print 'Manual List: ' + str(len(manList))
print 'GIZA_WordNet List: ' + str(len(autoDict))
print 'Manual - GIZA_WordNet: ' + str(len(DMminusDW))
print 'GIZA_WordNet - Manual: ' + str(len(DWminusDM))