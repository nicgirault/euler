N = 1000

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

primes = filter(isprime,range(9000))
print 'hello'
remarkables = {}
for a in range(len(primes)):
  print primes[a]
  remarkables[a] = filter(lambda x:isprime(int(str(primes[a])+str(primes[x]))) and isprime(int(str(primes[x])+str(primes[a]))), range(a))

print 'hello'
for a in remarkables:
  A = filter(lambda x: x[0]==a or x[1]==a,remarkables)
  for b in [x[0] for x in A if x[0]!=a]+[x[1] for x in A if x[1]!=a]:
    B = filter(lambda x: x[0]==b or x[1]==b,remarkables)
    print set(A) & set(B)

print 'hello again'
  
