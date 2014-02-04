## To extract the terminals from the programs

subs = []

s = 'PROJECT(AtomicColSet(COL_FARE()), EXTRACT_ROW_MIN_F(COL_FARE(), AtomicRowPredSet(AtomicRowPred(EQ_DEPARTS(CITY(atlanta), ANY(), ANY(), ANY(), ANY()), EQ_ARRIVES(CITY(dallas), ANY(), ANY(), ANY(), ANY())))))'

flag = False

shortArray = []

for c in s:
  if (c.isupper()) or (c == '_'):
    flag = True
    shortArray.append(c)
  else:
    if flag == True:
      temp = ''.join(shortArray)
      subs.append(temp)
      shortArray = []
      flag = False
      continue
    else:
      continue

print subs