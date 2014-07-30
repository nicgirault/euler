available = ['1','2','3','4','5','6','7','8','9']
stack = []
res = []
for a in range(9):
  p = available.pop(a)
  stack.append(p)
  for b in range(8):
    p = available.pop(b)
    stack.append(p)
    for c in range(7):
      p = available.pop(c)
      stack.append(p)
      for d in range(6):
        p=available.pop(d)
        stack.append(p)
        for e in range(5):
          p=available.pop(e)
          stack.append(p)
          for f in range(4):
            p=available.pop(f)
            stack.append(p)
            for g in range(3):
              p=available.pop(g)
              stack.append(p)
              for h in range(2):
                p=available.pop(h)
                stack.append(p)
                p=available.pop()
                stack.append(p)
                for fois in range(8)[1:]:
                  for egal in range(8)[fois+1:]:
                    a1 = ''
                    a2 = ''
                    pdt = ''
                    for x in stack[:fois]:
                      a1 += x
                    for x in stack[fois:egal]:
                      a2 += x
                    for x in stack[egal:]:
                      pdt += x
                    if int(a1)*int(a2) == int(pdt):
                      if int(pdt) not in res:
                        res.append(int(pdt))
                      print a1,a2,pdt
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
print sum(res)
