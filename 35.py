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
res = 0
for x in range(1000000)[2:]:
  s = str(x)
  cpt = 0
  for p in range(len(s)):
    if isprime(int(s)):
      cpt += 1
    s = s[-1]+s[:len(s)-1]
  if cpt == len(s):
    print s
    res += 1
print res
