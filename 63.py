cpt = 0
for k in range(10):
  p = 1
  n = 1
  while(len(str(p)) >= n-1):
    p = k**n
    if len(str(p)) == n:
      cpt += 1
      print k,n,p
    n += 1
print cpt
