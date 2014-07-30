s = ['0','1','2','3','4','5','6','7','8','9']
available = [x for x in range(10)]
stack = []
cpt = 0
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
              for h in range(3):
                p=available.pop(h)
                stack.append(p)
                for i in range(2):
                  p=available.pop(i)
                  stack.append(p)
                  p=available.pop()
                  stack.append(p)
                  cpt += 1
                  if cpt == 1000000:
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
                
