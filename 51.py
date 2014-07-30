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
 


def list_nums(number,nb_modif_d):
  list_numbers = []
  for conserved_pos in it.permutations(range(len(number)),nb_modif_d):
    my_num = ''
    for c in range(len(number)):
      if c in conserved_pos:
        my_num += number[c]
      else:
        my_num += 'x'
    if my_num not in list_numbers:
      list_numbers.append(my_num)
  return list_numbers

notFound = True
n = 120300



while notFound:
  print n
  max_cpt = 0
  for k in range(1,len(str(n))):
#    time1 = datetime.now()
    my_list = list_nums(str(n),k)
#    time2 = datetime.now()
    for to_test in my_list:
      cpt = 0
      res = []
      for nd in range(0,10):
        nnum = int(to_test.replace('x',str(nd)))
        if isprime(nnum) and len(str(nnum)) == len(str(n)):
          cpt += 1
          res.append(nnum)
      if cpt > max_cpt:
        max_cpt = cpt
      if cpt == 8:
        print res
        print n
        notFound = False
#    time3 = datetime.now()
#    print time2-time1,time3-time2
  n += 1




