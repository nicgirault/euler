s = [2]
i = 1
while len(s) < 110:
	s += [1,2*i,1]
	i += 1

def rec(x,num,den):
	return [den,num+x*den]

k=99
[num,den] = [1,s[k]]
while k > 0:
	[num,den] = rec(s[k-1],num,den)
	k -= 1
s = 0
for char in str(den):
	s += int(char)
print num,den
print s
