f = open('cipher1.txt')
msg = f.readline().split(',')
msg[-1] = msg[-1][:-1]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for k1 in alphabet:
  for k2 in alphabet:
    for k3 in alphabet:
      key = k1+k2+k3
      cpt = 0
      decry = ''
      for c in msg:
        decry += chr(int(c) ^ ord(key[cpt%3]))
        cpt += 1
      if all(badc not in decry for badc in'{}[]@#$%^&*+=/'):
        s = 0
        for dede in decry:
          s += ord(dede)
        print s
