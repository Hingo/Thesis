f1o = open("seed_mappings", "r")
seed_maps = []
line = f1o.readline()
while(line):
  line = line.strip()
  seed_maps.append(line)
  line = f1o.readline()
f1o.close()

f2o = open("giza_mappings_0.1", "r")
giza_maps = []
line = f2o.readline()
while(line):
  line = line.rstrip()
  giza_maps.append(line)
  line = f2o.readline()
f2o.close()

seedMINUSgiza = []
for item in seed_maps:
  if item not in giza_maps:
    seedMINUSgiza.append(item)

gizaMINUSseed = []
for item in giza_maps:
  if item not in seed_maps:
    gizaMINUSseed.append(item)

f3o = open("seeds-GIZA", "w")
for item in seedMINUSgiza:
    f3o.write(str(item) + "\n")
f3o.close()

f4o = open("GIZA-seeds", "w")
for item in gizaMINUSseed:
    f4o.write(str(item) + "\n")
f4o.close()

print 'Seed Maps Count: ' + str(len(seed_maps))
print 'GIZA Maps Count: ' + str(len(giza_maps))
print 'Seeds - GIZA Maps: ' + str(len(seedMINUSgiza))
print 'GIZA Maps - Seeds: ' + str(len(gizaMINUSseed))