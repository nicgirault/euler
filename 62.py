cubes = [x*x*x for x in range(5000,10000)]
def areP(a,b):
  d1 = [d for d in str(a)]
  d2 = [d for d in str(b)]
  d1.sort()
  d2.sort()
  if d1 == d2:
    return True
  return False

dico = {}
cc = 0
for c in cubes:
  cc += 1
  print cc
  cpt = 0
  for k in dico.keys():
    if areP(c,k):
      dico[k].append(c)
      cpt += 1
      break
  if cpt == 0:
    dico[c] = []

#cubes_per_length = [filter(lambda x: len(str(x))==a,cubes) for a in range(len(str(cubes[-1]))+1)]

#for subset in cubes_per_length:
#  for a in range(len(subset)):
#    for b in range(a):
#      for c in range(b):
#        if areP(subset[a],subset[b]) and areP(subset[a],subset[c]):
#          print subset[a],subset[b],subset[c]

print max([len(x) for x in dico.values()])
for k in dico.keys():
  if len(dico[k]) == 4:
    print k, dico[k]
