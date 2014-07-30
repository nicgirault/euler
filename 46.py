import math
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


def is2s(n):
  if n%2 == 0 and math.sqrt(n/2)%1 == 0:
    return True
  else:
    return False

n = 1
notFound = True
while notFound:
  n += 1
  if not isprime(n):
    if n%2 == 1:
      cpt = 0
      for p in range(1,n):
        if isprime(p):
          if is2s(n - p):
            cpt += 1
      if cpt == 0:
        notFount = False
        print n
      
