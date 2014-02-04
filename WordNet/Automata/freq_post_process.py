frequency_threshold = 1


fo2 = open("seed_mappings", "r")
seed_map_list = []
sline = fo2.readline()
while(sline):
  sline = sline.rstrip()
  seed_map_list.append(sline)
  sline = fo2.readline()
fo2.close()
print str(len(seed_map_list))

fo1 = open("map_frequency", "r")

frq = {}
weed_list_freq = []

line = fo1.readline()
while(line):
  line = line.rstrip()
  lineList = line.split()
  frq[lineList[0]] = lineList[1]
  line = fo1.readline()
fo1.close()
#print str(frq)
print str(len(frq))

for key, value in frq.iteritems():
  if key not in seed_map_list:
    if int(value) <= frequency_threshold:
      weed_list_freq.append([key, value])
print str(len(weed_list_freq))

fo3 = open("weed_map_frequency1_a", "w")
for wll in weed_list_freq:
  fo3.write(str(wll[0]) + '\n')
fo3.close()
  