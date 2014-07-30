tr = []
tr.append([0,1,0])
cpt = 0
for n in range(1,101):
  add = [0]
  for k in range(len(tr[-1])-1):
    if tr[-1][k]+tr[-1][k+1] > 1000000:
      cpt += 1
    add.append(tr[-1][k]+tr[-1][k+1])
  add.append(0)
  tr.append(add)
print cpt
