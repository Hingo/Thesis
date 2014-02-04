## To extract the terminals from the programs

subs = []

s = 'INSERT(STRING(:), Position(AFTER(NUMBERTOKEN()), ALL()), IterationScope(LINESCOPE(), ALWAYS(), ALL()))'

flag = False

shortArray = []

for c in s:
  if not c.isupper():
    if flag == True:
      temp = ''.join(shortArray)
      subs.append(temp)
      shortArray = []
      flag = False
      continue
    else:
      continue
  else:
    flag = True
    shortArray.append(c)

print subs