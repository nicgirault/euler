from fractions import Fraction

cpt = 0
denum = [2]
for x in range(1,1001):
  denum.append(Fraction(2*denum[-1]+1,denum[-1]))
  a = Fraction(1+denum[-1],denum[-1])
  if len(str(a.numerator)) > len(str(a.denominator)):
    cpt += 1
print cpt
