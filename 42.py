
def t(n):
  return n*(n+1)/2

f = open('words.txt')
words = []
for line in f.readlines():
  mots_g = line.split(',')
  for w in mots_g:
    words.append(w[1:-1])

def value(word):
  v = 0
  for c in word:
    v += ord(c)-64
  return v
t_values = [t(n) for n in range(1,21)]
w_values = []
for w in words:
  w_values.append(value(w))

cpt = 0
for v in w_values:
  if v in t_values:
    cpt += 1
print cpt
