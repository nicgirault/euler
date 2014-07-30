a = range(1000)[100:]
b = range(1000)[100:]
a.reverse()
b.reverse()
res = []
for x in a:
  for y in b:
    n = x*y
    n = str(n)
    rev = n[::-1]
    if n == rev:
      res.append(int(n))
print max(res)
