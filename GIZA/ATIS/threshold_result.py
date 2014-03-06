ATIS_terminals = ['AIRCRAFT', 'AIRLINES', 'BETWEEN_CITIES', 'BREAKFAST', 'CITY', 'CLASS', 'COL_AIRCRAFT_TYPE', 'COL_AIRLINES', 'COL_ARRIVAL_TIME', 'COL_DEPARTURE_TIME', 'COL_FARE', 'COL_STOPS', 'COL_TRANSPORT', 'DAYNUM', 'EQ_AIRCRAFT_TYPE', 'EQ_AIRLINES', 'EQ_AIRPORT', 'EQ_ARRIVES', 'EQ_CLASS', 'EQ_DEPARTS', 'EQ_FOOD', 'EQ_NON_STOP', 'EQ_STOPS', 'EXTRACT_ROW_MAX', 'EXTRACT_ROW_MAX_T', 'EXTRACT_ROW_MIN', 'EXTRACT_ROW_MIN_F', 'EXTRACT_ROW_MIN_T', 'MATCH_TIME_AROUND', 'MATCH_TIME_GT', 'MATCH_TIME_LT', 'MEAL', 'MONTH', 'NONE', 'PROJECT', 'ROUND_TRIP', 'TIME', 'WEEKDAY']

ATIS_waste_words = ['as', 'should', 'will', 'then', 'kindly', 'some', 'trying', 'with', 'that', 'o', 'next', 'could', 'wish', 'can', 'this', 'another', 'may', 'again', '755', '9pm', 'october', 'dc10', 'year', 'arrangements', 'now', 'april']

proper_nouns = []

maps = []
actual_match_whole = open("actual.match.final", "r")
threshold = 0.1
giza_map_file = open("giza_mappings_" + str(threshold), "w")

line = actual_match_whole.readline()
while(line):
  line = line.rstrip()
  english_word, dsl_terminal, alignment = line.split()
  if(float(alignment) >= threshold):
    if str(dsl_terminal) in ATIS_terminals:
      if ("\"" in english_word) or ("#" in english_word) or (english_word in ATIS_waste_words) or (english_word in proper_nouns):
	line = actual_match_whole.readline()
	continue
      maps.append(str(dsl_terminal) + "$" + str(english_word))
  line = actual_match_whole.readline()

seen = set()
seen_add = seen.add
unique_maps = [x for x in maps if x not in seen and not seen_add(x)]

for one_map in unique_maps:
  giza_map_file.write(str(one_map) + "\n")
  
actual_match_whole.close()
giza_map_file.close()