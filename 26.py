#import decimal as d
#myothercontext = d.Context(prec=10000, rounding=d.ROUND_HALF_DOWN)
#d.setcontext(myothercontext)
#for i in range(1000)[1:]:
#  k = d.Decimal(1)/d.Decimal(i)
#  print i,k
f = open('26.txt')


for line in f.readlines():
  n=line.split(' ')[1]
  num = line.split(' ')[0]
  k = n[:-1]
  for size in range(9000)[1:]:
    cpt = 0
    for c in range(250)[2:]:
      if k[-c-1:-c] == k[-c-size-1:-c-size]:
        cpt += 1
    if cpt > 200:
      if size > 500:
        print num, size, k
      break
