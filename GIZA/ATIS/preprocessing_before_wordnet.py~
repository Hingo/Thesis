database_terminals = ['AIRCRAFT', 'AIRLINES', 'CITY', 'DAYNUM', 'MONTH', 'TIME', 'WEEKDAY']

manual_map_file = open("minimal_manual_all_mappings", "r")
giza_map_file = open("giza_mappings_0.1", "r")

processed_map_file = open("giza_0.1_seed_mappings", "w")

line = giza_map_file.readline()
while(line):
  line = line.rstrip()
  if(line.split('$')[0] in database_terminals):
    line = giza_map_file.readline()
    continue
  processed_map_file.write(str(line) + "\n")
  line = giza_map_file.readline()

giza_map_file.close()

line = manual_map_file.readline()
while(line):
  line = line.rstrip()
  if(not line.split('$')[0] in database_terminals):
    line = manual_map_file.readline()
    continue
  processed_map_file.write(str(line) + "\n")
  line = manual_map_file.readline()

manual_map_file.close()
processed_map_file.close()