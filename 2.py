fibo = [1,2]

while(fibo[-1]+fibo[-2] < 4000000):
  fibo = fibo + [fibo[-1]+fibo[-2]]
print fibo
res = 0
for n in fibo:
  if n%2 == 0:
    res += n
print res
