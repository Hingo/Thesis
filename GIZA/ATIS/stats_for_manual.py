f1o = open("minimal_manual_all_mappings", "r")
manual_maps = []
line = f1o.readline()
while(line):
  line = line.strip()
  manual_maps.append(line)
  line = f1o.readline()
f1o.close()

f2o = open("giza_0.1_seed_mappings", "r")
giza_maps = []
line = f2o.readline()
while(line):
  line = line.rstrip()
  giza_maps.append(line)
  line = f2o.readline()
f2o.close()

manualMINUSgiza = []
for item in manual_maps:
  if item not in giza_maps:
    manualMINUSgiza.append(item)

gizaMINUSmanual = []
for item in giza_maps:
  if item not in manual_maps:
    gizaMINUSmanual.append(item)

f3o = open("manual-GIZA", "w")
for item in manualMINUSgiza:
    f3o.write(str(item) + "\n")
f3o.close()

f4o = open("GIZA-manual", "w")
for item in gizaMINUSmanual:
    f4o.write(str(item) + "\n")
f4o.close()

print 'Manual Maps Count: ' + str(len(manual_maps))
print 'GIZA Maps Count: ' + str(len(giza_maps))
print 'Manual - GIZA Maps: ' + str(len(manualMINUSgiza))
print 'GIZA Maps - Manual: ' + str(len(gizaMINUSmanual))