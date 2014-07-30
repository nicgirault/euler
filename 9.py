squares = {x*x:x for x in range(1000)[1:]}
for i in squares.values():
  for j in squares.values()[i:]:
    s = i*i+j*j
    if s in squares.keys() and i+j+squares[s]==1000:
      print i,j,squares[s]
      print i*j*squares[s]

