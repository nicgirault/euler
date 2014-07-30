res = [1]
for n in range(2,1001):
  res.append(res[-1]+n**n)
print res[-1]
