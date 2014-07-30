import math
test = True
n = 1
t_value = 0

while test:
  t_value += n
  n+= 1

  cpt = 0
  for k in range(int(math.sqrt(t_value))+1)[1:]:
    if t_value%k == 0:
      cpt +=1
  print cpt
  if cpt > 250:
    print t_value
    test = False
