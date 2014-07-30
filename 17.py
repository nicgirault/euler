a = 'onetwothreefourfivesixseveneightnine'
b = 'teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen'
c = 'twentythirtyfortyfiftysixtyseventyeightyninety'
d = 'hundred'
e = 'onethousand'
f = 'and'
n = len(a)+len(b)+(10*len(c)+8*len(a))
res = n+(100*len(a)+900*len(d)+891*len(f)+n*9)+len(e)
print res
