tot = {}
for p in range(1001)[3:]:
  cpt = 0
  for a in range(p/2+1)[1:]:
    for b in range(a)[1:]:
      for c in range(b+1)[a-b:]:
        if a + b + c == p and c*c + b*b == a*a:
          #print p,a,b,c
          cpt += 1
  tot[cpt] = p
  print max(tot.keys()),tot[max(tot.keys())]

