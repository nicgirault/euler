
test = True
n = 1001
t_value = 0

nat = [x for x in range(1001)]
t_value = sum(nat)



while test:
  t_value += n
  n+= 1

  cpt = 0
  for k in range(t_value+1)[1:]:
    if t_value%k == 0:
      cpt +=1
  print cpt
  if cpt > 500:
    print t_value
    test = False
