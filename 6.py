a = [x for x in range(101)[1:]]
squares = [x*x for x in a]

print a
print squares

sum1 = sum(squares)
sum2 = sum(a)*sum(a)
print sum1-sum2
