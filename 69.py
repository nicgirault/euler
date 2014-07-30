N = 1000000

import itertools as it
from datetime import datetime

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
primes = filter(isprime,range(1000000))

def phi(n):
  pri = 1
  for m in range(3,n,2):
    if n%m != 0:
      pri += 1
  return float(n)/pri

ratios = {}
for n in range(900001,N,2):
  print n
  if n == primes[0]:
    primes.pop(0)
  else:
    ratios[phi(n)] = n
m = max(ratios.keys())
print ratios[m]
