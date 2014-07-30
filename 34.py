def fact(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    return n*fact(n-1)
res = 0
for x in range(5000000)[2:]:
  s = 0
  for digit in str(x):
    s += fact(int(digit))
  if s == x:
    res += s
    print s
print res
