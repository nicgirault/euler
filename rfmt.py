res = []
f = open('triangle.txt')
for line in f.readlines():
  res.append(line[:-1].split(' '))
print res
