englishFile = open("englishTokens.vcb", "r")
englishDic = {}
line = englishFile.readline()
while(line):
  line = line.rstrip()
  token_number, token_name, freq_count = line.split()
  englishDic[token_number] = [token_name, freq_count]
  line = englishFile.readline()
#print str(englishDic)
englishFile.close()

DSLFile = open("DSLTokens.vcb", "r")
DSLDic = {}
line = DSLFile.readline()
while(line):
  line = line.rstrip()
  token_number, token_name, freq_count = line.split()
  DSLDic[token_number] = [token_name, freq_count]
  line = DSLFile.readline()
#print str(DSLDic)
DSLFile.close()

actual_match_file = open("actual.match.final", "w")
token_match_file = open("match.final", "r")

line = token_match_file.readline()
while(line):
  #print line
  line = line.rstrip()
  token_number_1, token_number_2, alignment_score = line.split()
  if(token_number_1 == '0' or token_number_2 == '0'):
    line = token_match_file.readline()
    continue
  to_show = str((englishDic[token_number_1])[0].lower().rstrip('.')) + " " + str((DSLDic[token_number_2])[0]) + " " + str(alignment_score)
  actual_match_file.write(to_show + "\n")
  line = token_match_file.readline()
actual_match_file.close()
token_match_file.close()