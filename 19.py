m = [31,28,31,30,31,30,31,31,30,31,30,31]
m_leap = [31,29,31,30,31,30,31,31,30,31,30,31]
y = [x for x in range(2001)[1900:]]
w = [1,2,3,4,5,6,7]

s=[]
cpt = 0
for year in y:
  if year%4 == 0 and year != 2000:
    months = m_leap
  else:
    months = m

  for M in months:
    cpt += M
    s.append(cpt)

dimanches = 0
for k in s[11:]:
  if k%7 == 0:
    dimanches += 1

print dimanches
