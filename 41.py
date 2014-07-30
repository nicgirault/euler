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

available = ['1','2','3','4','5','6','7']
stack = []
res = []
for a in range(7):
  p = available.pop(a)
  stack.append(p)
  for b in range(6):
    p = available.pop(b)
    stack.append(p)
    for c in range(5):
      p = available.pop(c)
      stack.append(p)
      for d in range(4):
        p=available.pop(d)
        stack.append(p)
        for e in range(3):
          p=available.pop(e)
          stack.append(p)
          for h in range(2):
            p=available.pop(h)
            stack.append(p)
            p=available.pop()
            stack.append(p)
            str_num = ''
            for x in stack:
              str_num += x
            num = int(str_num)
            if isprime(num):
              print num
            available.append(stack.pop())
            available.append(stack.pop())
            available.sort()
          available.append(stack.pop())
          available.sort()
        available.append(stack.pop())
        available.sort()
      available.append(stack.pop())
      available.sort()
    available.append(stack.pop())
    available.sort()
  available.append(stack.pop())
  available.sort()
print sum(res)
