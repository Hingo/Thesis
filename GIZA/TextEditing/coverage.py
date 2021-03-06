import os

def uniqifying(seq):			# Takes a set of 'objects' and makes it unique except list
  seen = set()
  seen_add = seen.add
  return [ x for x in seq if x not in seen and not seen_add(x)]

benchmark_file = open("benchmarkSample.txt", "r")
benchmarks = {}
line = benchmark_file.readline()
while(line):
  line = line.rstrip()
  prog = benchmark_file.readline()
  prog = prog.rstrip()
  benchmarks[line] = prog
  benchmark_file.readline()
  line = benchmark_file.readline()
benchmark_file.close()

map_file = open("manual-GIZA", "r")
not_used = []
line = map_file.readline()
while(line):
  line = line.rstrip()
  line = line.split('$')
  regEx = ' ' + line[1] + ' '
  for statement, program in benchmarks.iteritems():
    if regEx in statement:
      if line[0] in program:
	not_used.append(statement)
  line = map_file.readline()
map_file.close()

#print not_used

not_covered = uniqifying(not_used)

for statement in not_covered:
  print statement