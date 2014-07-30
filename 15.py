x = [i for i in range(21)]
y = [i for i in range(21)]

grille = [[0 for a in range(21)] for b in range(21)]
grille[0] = [1 for a in x]
for a in x:
  grille[a][0] = 1

for i in x[1:]:
  for j in y[1:]:
    grille[i][j] = grille[i-1][j] + grille[i][j-1]



for x in grille:
  print x
