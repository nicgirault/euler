import math

def isP(n):
  if (math.sqrt(1 + 24 * n) + 1.0)%6 == 0:
    return True
  else:
    return False

i = 3
notfound = True
while notfound:
  print i
  i += 1
  a = i*(3*i-1)/2
  for j in range(1,i):
    b = j*(3*j-1)/2
    if isP(a-b) and isP(a+b):
      print i,j
