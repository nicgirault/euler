m = [[0 for y in range(1001)] for x in range(1001)]

m[500][500] = 1
c = [500,501]

#size of the current square
c_square = 3
in_side = 2
# number to write
n = 2

while c_square < 1002:
  # Down
  while in_side < c_square:
    m[c[0]][c[1]] = n
#    print 'down'
#    print c
#    for line in m:
#      print line
#    print '\n'
    n += 1
    #down
    c[0] += 1
    in_side += 1
  in_side = 1

  # Left
  while in_side < c_square:
    m[c[0]][c[1]] = n
#    print 'left'
#    print c
#    for line in m:
#      print line
#    print '\n'
    n += 1
    #left
    c[1] -= 1
    in_side += 1
  in_side = 1
  
# Up
  while in_side < c_square:
    m[c[0]][c[1]] = n
#    print 'up'
#    print c
#    for line in m:
#      print line
#    print '\n'
    n += 1
    #up
    c[0] -= 1
    in_side += 1
  in_side = 1

  # Right
  while in_side <= c_square:
    m[c[0]][c[1]] = n
#    print 'right'
#    print c
#    for line in m:
#      print line
#    print '\n'
    n += 1
    # Right
    c[1] += 1
    in_side += 1
  in_side = 2
  c_square += 2

diag1 = []
diag2 = []
for x in range(len(m)):
  diag1.append(m[x][x])
  diag2.append(m[x][-x-1])
res = sum(diag1) + sum(diag2)
print res-1
for line in m:
  l = ''
  for num in line:
    l += '%3s ' %num
  #print l
