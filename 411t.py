for n in [123]:
  print n
  S = []
  for i in range(2*n+1):
    tmp = [2**i%n,3**i%n]
    if tmp not in S:
      S.append(tmp)
  print S

  G = {}
  for station in S:
    neighbor = []
    for pot_nei in S:
      if pot_nei[0] >= station[0] and pot_nei[1] >= station[1] and pot_nei != station:
        neighbor.append(S.index(pot_nei))
    G[S.index(station)] = neighbor
  
#  for station in range(len(S)):
#    print S[station], [S[st] for st in G[station]]
  
  paths = [[x] for x in range(len(S))]
  cpt = 1
  while cpt > 0:
    new_paths = []
    proposed_np = {}
    toremove = []
    cpt = 0
    for p in paths:
      if p[-1] not in toremove:
        for n in G[p[-1]]:
          toremove.append(n)
          cpt += 1
          if p[-1] in proposed_np.keys():
            proposed_np[p[-1]].append(p+[n])
          else:
            proposed_np[p[-1]] = [p+[n]]
    if cpt > 0:
      for p in paths:
        if p[-1] not in toremove:
          if p[-1] in proposed_np.keys():
            for x in proposed_np[p[-1]]:
              new_paths.append(x)
      paths = new_paths
  print max([len(x) for x in paths])
