values = [100,50,20,10,5,2,1]
leaves = [(100,),(50,),(20,),(10,),(5,),(2,),(1,)]
completed = [(200,)]

while len(leaves) != 0:
  memory = leaves.pop(0)
  leaf = list(memory)
  new_leaves = []
  for v in values:
    if v <= leaf[-1]:
      leaf.append(v)
      if sum(leaf) == 200:
        completed.append(tuple(leaf))
        print leaf
      if sum(leaf) < 200:
        leaves.append(tuple(leaf))
      leaf = list(memory)
print len(completed)
