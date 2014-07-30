primes = [2,3,5,7,11,13]

x = 14

while len(primes) < 10001:
  div = [x%k for k in primes]
  if all(div):
    primes.append(x)
    print len(primes)
  x+=1
print primes[10000]
