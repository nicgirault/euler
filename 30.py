su = 0
for x in range(1000000)[2:]:
  s = str(x)
  r = 0
  for digit in s:
    r += int(digit)**5
  if r == x:
    print x
    su += x
print su

    
