import os, glob

terminals = ['AFTER', 'ALL', 'ALLBUT', 'ALWAYS', 'AND', 'ANY', 'BEFORE', 'BETWEEN', 'BLANKLINETOKEN', 'BY', 'CHARTOKEN', 'CONCATENATE', 'CONTAINS', 'DIGITTOKEN', 'DOCUMENT', 'END', 'ENDSWITH', 'EVERY', 'FIRSTFEW', 'FIRSTONE', 'IMM', 'INSERT', 'INTEGER', 'INTSET', 'LASTFEW', 'LASTONE', 'LINE', 'LINESCOPE', 'LINETOKEN', 'MATCHES', 'NONBLANKLINETOKEN', 'NONDIGITTOKEN', 'NOT', 'NUMBERTOKEN', 'OR', 'PRINT', 'REMOVE', 'REPEAT', 'REPLACE', 'SEQ', 'START', 'STARTFROM', 'STARTSWITH', 'STRING', 'TEXTTOKEN', 'TO', 'WHITESPACETOKEN', 'WORD', 'WORDSCOPE', 'WORDTOKEN']

folder_path = "./xml_Dictionary/"

for item_to_remove in glob.glob(folder_path + '*'):
  os.remove(item_to_remove)

for terminal in terminals:
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

for terminal in terminals:
  terminal_file = open(folder_path + str(terminal) + ".xml", "a+")
  terminal_file.write("</" + str(terminal) + ">")
  terminal_file.close()