
f = open('names.txt')
for line in f.readlines():
  names = line.split(',')
for k in range(len(names)):
  names[k]=names[k][1:-1]

names.sort()
res = 0
for i in range(len(names)):
  somme = 0
  for j in names[i]:
    somme += ord(j)-64
  res += (i+1)*somme
print res


