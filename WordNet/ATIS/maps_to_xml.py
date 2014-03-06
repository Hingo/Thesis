import os, glob

ATIS_terminals = ['AIRCRAFT', 'AIRLINES', 'BETWEEN_CITIES', 'BREAKFAST', 'CITY', 'CLASS', 'COL_AIRCRAFT_TYPE', 'COL_AIRLINES', 'COL_ARRIVAL_TIME', 'COL_DEPARTURE_TIME', 'COL_FARE', 'COL_STOPS', 'COL_TRANSPORT', 'DAYNUM', 'EQ_AIRCRAFT_TYPE', 'EQ_AIRLINES', 'EQ_AIRPORT', 'EQ_ARRIVES', 'EQ_CLASS', 'EQ_DEPARTS', 'EQ_FOOD', 'EQ_NON_STOP', 'EQ_STOPS', 'EXTRACT_ROW_MAX', 'EXTRACT_ROW_MAX_T', 'EXTRACT_ROW_MIN', 'EXTRACT_ROW_MIN_F', 'EXTRACT_ROW_MIN_T', 'MATCH_TIME_AROUND', 'MATCH_TIME_GT', 'MATCH_TIME_LT', 'MEAL', 'MONTH', 'NONE', 'PROJECT', 'ROUND_TRIP', 'TIME', 'WEEKDAY']

folder_path = "./xml_Dictionary/"

for item_to_remove in glob.glob(folder_path + '*'):
  os.remove(item_to_remove)

for terminal in ATIS_terminals:
  terminal_file = open(folder_path + str(terminal) + ".xml", "a+")
  terminal_file.write("<" + str(terminal) + ">\n")
  terminal_file.close()

map_file = open("manual_U_giza_automatedMaps", "r")
line = map_file.readline()
while(line):
  line = line.rstrip()
  line = line.split()
  terminal, word = line[0].split('$')
  terminal_file = open(folder_path + str(terminal) + ".xml", "a+")
  terminal_file.write("<ELEMENT literal = \"" + str(word) + "\" type = \"_\"></ELEMENT>\n")
  if(str(word)[0].islower()):
    terminal_file.write("<ELEMENT literal = \"" + str(word)[0].upper() + str(word)[1:] + "\" type = \"_\"></ELEMENT>\n")
  elif(str(word)[0].isupper()):
    terminal_file.write("<ELEMENT literal = \"" + str(word)[0].lower() + str(word)[1:] + "\" type = \"_\"></ELEMENT>\n")
  else:
    hingo = 'lier'
  terminal_file.close()
  line = map_file.readline()
map_file.close()

for terminal in ATIS_terminals:
  terminal_file = open(folder_path + str(terminal) + ".xml", "a+")
  terminal_file.write("</" + str(terminal) + ">")
  terminal_file.close()