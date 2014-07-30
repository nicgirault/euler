import itertools as it

# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def permut(n):
  perm = it.permutations(str(n))
  for tup in perm:
    number = ''
    for digit in tup:
      number += digit
    yield int(number)
    
already_done = []
for n in range(1001,10000):
  if n not in already_done and isprime(n):
    primes = []
    for p in permut(n):
      already_done.append(p)
      if isprime(p) and p not in primes and p > 1000:
        primes.append(p)
      primes.sort()
    if len(primes) > 2:
      dist = {}
      for i in primes[::-1]:
        for j in primes[::-1]:
          if j < i:
            if i-j in dist.keys():
              dist[i-j].append([i,j])
            else:
              dist[i-j] = [[i,j]]
      for k in dist.keys():
        if len(dist[k]) == 2:
          if dist[k][0][0] == dist[k][1][0] or dist[k][0][0] == dist[k][1][1] or dist[k][0][1] == dist[k][1][0] or dist[k][0][1] == dist[k][1][1]:
            print dist[k]
            
