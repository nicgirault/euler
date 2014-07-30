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


def list_div(n):
  r = n
  div = []
  x = 2
  if isprime(n):
    div.append(n)
    return div
  else:
    while True:
      if isprime(x) and n%x == 0:
        div.append(x)
        n = n/x
      else:
        x += 1
      if isprime(n):
        div.append(n)

# si plusieurs fois le meme diviseur, on ne return pas un nb premier ms le produit
        res = []
        for k in range(1,len(div)):
          if div[k-1]%div[k] == 0:
            div[k] *= div[k-1]
          else:
            res.append(div[k-1])
        res.append(div[-1])
        #print r,res
        return res



for x in range(100000,1000000):
  print x
  l1 = set(list_div(x))
  l2 = set(list_div(x+1))
  l3 = set(list_div(x+2))
  l4 = set(list_div(x+3))
#  print l1,l2,l3,l4
#  print len(l1),len(l2),len(l3),len(l4)
  if len(l1) == 4 and len(l2) == 4 and len(l3) == 4 and len(l4) == 4:
    print x
    break
