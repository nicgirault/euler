f = [1,1]
res = ''
while len(res)<1000:
  f.append(f[-1]+f[-2])
  res = str(f[-1])
print len(f)
