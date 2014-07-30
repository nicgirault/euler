def digits(n):
  res = []
  for d in str(n):
    res.append(int(d))
  res.sort()
  return(res)

for n in range(100001,166668):
  a = digits(n)
  if a == digits(2*n):
    if a == digits(3*n):
      if a == digits(4*n):
        if a == digits(5*n):
          if a == digits(6*n):
            print n
