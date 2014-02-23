import os, glob

folder_path = "./GIZA_0.5_TerminalsBackUp/"

for item_to_remove in glob.glob(folder_path + '*'):
  os.remove(item_to_remove)

map_file = open("giza_0.5_seed_mappings", "r")
line = map_file.readline()
while(line):
  line = line.rstrip()
  terminal, word = line.split('$')
  terminal_file = open(folder_path + str(terminal), "a+")
  terminal_file.write(str(word) + " 1.0\n")
  terminal_file.close()
  line = map_file.readline()
map_file.close()