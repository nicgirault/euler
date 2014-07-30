
cpts = {}
for i in range(1000000)[2:]:
  n = i
  cpt = 0
  while n != 1:
    cpt += 1
    if n%2 == 0:
      n = n/2
    else:
      n = 3*n + 1  
  print i
  cpts[cpt]=i
m = max(cpts.keys())
print cpts[m]
