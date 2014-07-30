def isP(n):
  if str(n) == str(n)[::-1]:
    return True
  return False

res = 0
for n in range(1,10001):
  x = n
  cpt = 0
  while True:
    x = x + int(str(x)[::-1])
    cpt += 1
    if isP(x):
      res += 1
      break
    if cpt > 50:
      break

print 10000-res
