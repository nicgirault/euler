res = []
for a in range(101)[2:]:
  for b in range(101)[2:]:
    r = a**b
    if r not in res:
      res.append(r)
print len(res)
