
s = {}
for x in range(10001)[2:]:
  div = []
  for d in range(x)[1:]:
    if x%d == 0 and d != x:
      div.append(d)
  s[x] = sum(div)

res = 0
for x in s.keys():
  if s[x] < 10000 and s[x]>1 and s[x] != x:
    if s[s[x]] == x:
      res += x
print res



