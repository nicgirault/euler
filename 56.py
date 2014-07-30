res = []
for a in range(1,100):
  for b in range(1,100):
    s = str(a**b)
    somme = 0
    for d in s:
      somme += int(d)
    res.append(somme)
print max(res)
