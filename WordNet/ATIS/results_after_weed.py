fo = open("map_frequency", "r")
line = fo.readline()
autoM = []
while(line):
  line = line.rstrip()
  l = line.split()
  autoM.append(l[0])
  line = fo.readline()
fo.close()
print 'Automated List: ' + str(len(autoM))

fo = open("weed_map_frequency2_a", "r")
line = fo.readline()
weedM = []
while(line):
  line = line.rstrip()
  weedM.append(line)
  line = fo.readline()
fo.close()

maps_aft_weed = [item for item in autoM if item not in weedM]
fo = open("Maps_after_weed2", "w")
for m in maps_aft_weed:
  fo.write(str(m) + '\n')
fo.close()
print 'Maps after weed: ' + str(len(maps_aft_weed))
