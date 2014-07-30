class Node(object):
    def __init__(self, data, parent):
        self.data = data
        self.children = []
        self.parent = parent
        self.dist = 0
    def add_child(self, obj):
        self.children.append(obj)

path_lenght = []

def add_neighbor(nodes,S):
  if len(nodes) == 0:
    return False
  else:
    for node in nodes:
      neighb = []
      for k in S:
        if k[0] >= node.data[0] and k[1] >= node.data[1] and k != node.data:
          tmp = Node(k,node)
          tmp.dist = node.dist + 1
          node.add_child(tmp)
          path_lenght.append(tmp.dist)
          neighb.append(tmp)
      add_neighbor(neighb,S)


res = 0
for n in [10000]:
  print n
  S = []
  for i in range(2*n+1):
    tmp = [2**i%n,3**i%n]
    if tmp not in S:
      S.append(tmp)
  print S

  root = Node(S[0],None)
  add_neighbor([root],S)
  
  print max(path_lenght)+1
