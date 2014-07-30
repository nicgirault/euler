def fact(n):
  if n == 2:
    return 2
  else:
    return fact(n-1)*n

s = str(fact(100))
somme = sum([int(x) for x in s])
print somme
