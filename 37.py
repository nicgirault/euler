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

right = []
for x in range(10)[2:]:
  if isprime(x):
    for x2 in range(10)[1:]:
      p = int(str(x2)+str(x))
      if isprime(p):
        right.append(p)
        for x3 in range(10)[1:]:
          p = int(str(x3)+str(x2)+str(x))
          if isprime(p):
            right.append(p)
            for x4 in range(10)[1:]:
              p = int(str(x4)+str(x3)+str(x2)+str(x))
              if isprime(p):
                right.append(p)
                for x5 in range(10)[1:]:
                  p = int(str(x5)+str(x4)+str(x3)+str(x2)+str(x))
                  if isprime(p):
                    right.append(p)
                    for x6 in range(10)[1:]:
                      p = int(str(x6)+str(x5)+str(x4)+str(x3)+str(x2)+str(x))
                      if isprime(p):
                        right.append(p)
                        for x7 in range(10)[1:]:
                          p = int(str(x7)+str(x6)+str(x5)+str(x4)+str(x3)+str(x2)+str(x))
                          if isprime(p):
                            right.append(p)

left = []
for x in range(10)[2:]:
  if isprime(x):
    for x2 in range(10)[1:]:
      p = int(str(x)+str(x2))
      if isprime(p):
        left.append(p)
        for x3 in range(10)[1:]:
          p = int(str(x)+str(x2)+str(x3))
          if isprime(p):
            left.append(p)
            for x4 in range(10)[1:]:
              p = int(str(x)+str(x2)+str(x3)+str(x4))
              if isprime(p):
                left.append(p)
                for x5 in range(10)[1:]:
                  p = int(str(x)+str(x2)+str(x3)+str(x4)+str(x5))
                  if isprime(p):
                    left.append(p)
                    for x6 in range(10)[1:]:
                      p = int(str(x)+str(x2)+str(x3)+str(x4)+str(x5)+str(x6))
                      if isprime(p):
                        left.append(p)
                        for x7 in range(10)[1:]:
                          p = int(str(x)+str(x2)+str(x3)+str(x4)+str(x5)+str(x6)+str(x7))
                          if isprime(p):
                            left.append(p)
print sum(set(left) & set(right))
