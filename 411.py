from datetime import datetime as d
def longest_path(graph):
  t1 = d.now()
  dist = {}
  Q = [0]

  for v in range(len(S)):
    dist[v] = 0

  while len(Q) > 0:
    current_node = Q[0]
    for v in graph[current_node]: # for each neighbor
      if dist[v] < dist[current_node] + 1:
        dist[v] = dist[current_node] + 1
        if v not in Q:
          Q.append(v)
    Q.remove(current_node)
  t2 = d.now()
  return max(dist.values()),t2-t1


def redu(graph):
  for v in graph.keys():
    toRemove = []
    for neighbor in graph[v]:
      for to_check in graph[v]:
        if to_check not in toRemove and to_check in graph[neighbor]:
          toRemove.append(to_check)
    for x in toRemove:
      graph[v].remove(x)


res = 0
for n in [k**5 for k in range(10)]:
  t_deb = d.now()
  S = [[0,0],[1,1]]
  for i in range(1,2*n+1):
    tmp = [2*S[-1][0]%n,3*S[-1][1]%n]
    if tmp not in S:
      S.append(tmp)
  S = tuple(S)
#  print S

  G = {}
  G_reverse = {}
  for x in range(len(S)):
    G[x] = []
    G_reverse[x] = []

  for station in range(len(S)):
    neighbor = []
    neighbor = filter(lambda x: S[x][0] >= S[station][0] and S[x][1] >= S[station][1] and x != station,range(len(S)))
    for neig in neighbor:
      for preview in G_reverse[station]:
        if neig in G[preview]:
          G[preview].remove(neig)

      toremove = []
      for neig2 in neighbor:
        if neig2 in G[neig]:
          toremove.append(neig2)
      for x in toremove:
        neighbor.remove(x)

      G[station].append(neig)
      G_reverse[neig].append(station)
#      print G

#  redu(G)
#  print G
  #for station in range(len(S)):
  #  print S[station], [S[st] for st in G[station]]

  bb,t = longest_path(G)
  print bb
  res += bb
  t_end = d.now()
  print t_end - t_deb,t
