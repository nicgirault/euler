for d in range(10)[1:]:
  for u in range(10)[1:]:
    num = 10*d + u

    for d2 in range(10)[1:]:
      for u2 in range(10)[1:]:
        den = 10*d2 + u2
        if u == d2 and float(num)/den == float(d)/u2 and u != d:
          print num,den
