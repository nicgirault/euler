res = 0
for x in range(1000000):
  if str(bin(x))[2:] == str(bin(x))[2:][::-1] and str(x) == str(x)[::-1]:
    print x
    res += x
print res
