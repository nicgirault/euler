def is9pandigital(n):
  a = n.count('1')
  b = n.count('2')
  c = n.count('3')
  d = n.count('4')
  e = n.count('5')
  f = n.count('6')
  g = n.count('7')
  h = n.count('8')
  i = n.count('9')

  if a==1 and b==1 and c==1 and d==1 and e==1 and f==1 and g==1 and h==1 and i==1:
    if len(n) == 9:
      return True
    else:
      return False
  else:
    return False




for n in range(1000,50000):
  res = ''
  res += str(n*1)
  res += str(n*2)
  #res += str(n*3)
  if is9pandigital(res):
    print res

