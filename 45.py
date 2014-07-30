def T(n):
  return n*(n+1)/2
def P(n):
  return n*(3*n-1)/2
def H(n):
  return n*(2*n-1)

cpt = 0
t = 286
p = 166
h = 143
while True:
  current = T(t)
  if P(p) < T(t):
    p += 1
  if P(p) == T(t):
    if H(h) < T(t):
      h += 1
    if H(h) == T(t):
      print T(t)
      break
    if H(h) > T(t):
      t += 1
  if P(p) > T(t):
    t += 1
  
