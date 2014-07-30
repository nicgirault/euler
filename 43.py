available = ['0','1','2','3','4','5','6','7','8','9']
stack = []
res = []
for a in range(10):
  p = available.pop(a)
  stack.append(p)
  for b in range(9):
    p = available.pop(b)
    stack.append(p)
    for c in range(8):
      p = available.pop(c)
      stack.append(p)
      for d in range(7):
        p=available.pop(d)
        stack.append(p)
        for e in range(6):
          p=available.pop(e)
          stack.append(p)
          for f in range(5):
            p=available.pop(f)
            stack.append(p)
            for g in range(4):
              p=available.pop(g)
              stack.append(p)
              for g in range(3):
                p=available.pop(g)
                stack.append(p)
                for h in range(2):
                  p=available.pop(h)
                  stack.append(p)
                  p=available.pop()
                  stack.append(p)
                  if int(stack[1]+stack[2]+stack[3])%2 == 0:
                    if int(stack[2]+stack[3]+stack[4])%3 == 0:
                      if int(stack[3]+stack[4]+stack[5])%5 == 0:
                        if int(stack[4]+stack[5]+stack[6])%7 == 0:
                          if int(stack[5]+stack[6]+stack[7])%11 == 0:
                            if int(stack[6]+stack[7]+stack[8])%13 == 0:
                              if int(stack[7]+stack[8]+stack[9])%17 == 0:
                                mynum = ''
                                for x in stack:
                                  mynum += x
                                res.append(int(mynum))
                  print stack
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
      available.append(stack.pop())
      available.sort()
    available.append(stack.pop())
    available.sort()
  available.append(stack.pop())
  available.sort()
print sum(res)
