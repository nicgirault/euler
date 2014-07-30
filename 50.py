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

primes = [x for x in range(1000000) if isprime(x)]
print range(151,200)[::2]
for consec in range(151,800)[::2]:


  for x in range(2,len(primes[:-consec])):
    if primes[x] > 1000000/consec:
      break
    somme = 0
    for k in range(consec):
      somme += primes[x+k]
    if somme in primes[x+k:]:
      print somme, consec
      break
  
