primes = [2,3,5,7,11,13]

x = 14

while primes[-1] < 2000000:
  div = [x%k for k in primes]
  if all(div):
    primes.append(x)
    print primes[-1]
  x+=1
print sum(primes)
