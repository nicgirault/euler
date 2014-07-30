# The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math
prime_max = int(math.sqrt(600851475143))
print prime_max

prime_candidate = set([x for x in range(prime_max+1)[2:]])

while True:
  div = prime_candidate.pop()
  prime_candidate -= set([div*x for x in range(prime_max/div+1)])
  if 600851475143%div == 0:
    print div
