import os

eng_file = open("englishBenchmark.txt", "w")
dsl_file = open("DSL.txt", "w")
mix_file = open("testBenchmarkSample.txt", "r")
eng_line = mix_file.readline()
while(eng_line):
  eng_file.write(eng_line)
  dsl_prog = mix_file.readline()
  dsl_file.write(dsl_prog)
  blank = mix_file.readline()
  eng_line = mix_file.readline()

eng_file.close()
dsl_file.close()
mix_file.close()