f = open('poker.txt')

def royal_flush(hand):
  if 'T' in [hand[k][0] for k in range(5)]:
    if 'J' in [hand[k][0] for k in range(5)]:
      if 'Q' in [hand[k][0] for k in range(5)]:
        if 'K' in [hand[k][0] for k in range(5)]:
          if 'A' in [hand[k][0] for k in range(5)]:
            if all([hand[0][0] == hand[k][0] for k in range(1,5)]):
              return True
  return False

def flush(hand):
  if all([hand[k][1] == hand[0][1] for k in range(5)]):
    return True
  return False

def straight(hand):
  values = [hand[k][0] for k in range(5)]
  if 2 in values and 3 in values and 4 in values and 5 in values and 6 in values:
    return True
  if 7 in values and 3 in values and 4 in values and 5 in values and 6 in values:
    return True
  if 7 in values and 8 in values and 4 in values and 5 in values and 6 in values:
    return True
  if 7 in values and 8 in values and 9 in values and 5 in values and 6 in values:
    return True
  if 7 in values and 8 in values and 9 in values and 10 in values and 6 in values:
    return True
  if 7 in values and 8 in values and 9 in values and 10 in values and 11 in values:
    return True
  if 12 in values and 8 in values and 9 in values and 10 in values and 11 in values:
    return True
  if 12 in values and 13 in values and 9 in values and 10 in values and 11 in values:
    return True
  if 12 in values and 13 in values and 14 in values and 10 in values and 11 in values:
    return True
  return False

def three_of_a_kind(hand):
  values = [hand[k][0] for k in range(5)]
  for v in values:
    c = values.count(v)
    if c == 3:
      return True
  return False

def one_pair(hand):
  if two_pairs(hand):
    return False
  values = [hand[k][0] for k in range(5)]
  for v in values:
    c = values.count(v)
    if c == 2:
      return True
  return False

def two_pairs(hand):
  nb = []
  values = [hand[k][0] for k in range(5)]
  for v in values:
    nb.append(values.count(v))
  if nb.count(2) == 4:
    return True
  return False

def straight_flush(hand):
  if straight(hand) and flush(hand):
    return True
  return False

def four_of_a_kind(hand):
  for k in [hand[0][0],hand[1][0]]:
    if hand.count(k) == 4:
      return True
  return False

def full_house(hand):
  if one_pair(hand) and three_of_a_kind(hand):
    return True
  return False

def nothing(hand):
  if not straight_flush(hand) and not royal_flush(hand) and not full_house(hand) and not four_of_a_kind(hand) and not flush(hand) and not straight(hand) and not three_of_a_kind(hand) and not two_pairs(hand) and not one_pair(hand):
    return True
  return False

def pair_egality(h1,h2):
  values1 = [h1[k][0] for k in range(5)]
  values2 = [h2[k][0] for k in range(5)]
  for v in range(5):
    if values1.count(values1[v]) == 2:
      cur_v1 = values1[v]
    if values2.count(values2[v]) == 2:
      cur_v2 = values2[v]
  if cur_v1 > cur_v2:
    return 1
  elif cur_v1 < cur_v2:
    return 2
  else:
    values1.remove(cur_v1)
    values1.remove(cur_v1)
    values2.remove(cur_v2)
    values2.remove(cur_v2)
  
    values1.sort()
    values2.sort()
    if values1[-1] > values2[-1]:
      return 1
    elif values1[-1] < values2[-1]:
      return 2
    else:
      if values1[-2] > values2[-2]:
        return 1
      elif values1[-2] < values2[-2]:
        return 2
      else:
        print h1,h2

def nothing_egality(h1,h2):
  values1 = [h1[k][0] for k in range(5)]
  values2 = [h2[k][0] for k in range(5)]
  values1.sort()
  values2.sort()
  if values1[-1] > values2[-1]:
    return 1
  elif values1[-1] < values2[-1]:
    return 2
  else:
    if values1[-2] > values2[-2]:
      return 1 
    elif values1[-2] < values2[-2]:
      return 2
    else:
      if values1[-3] > values2[-3]:
        return 1 
      elif values1[-3] < values2[-3]:
        return 2
      else:
        print h1,h2
        print values1,values2
        print 'egalite',h1,h2

def max_combin(hand):
  if royal_flush(hand):
    return 10
  if straight_flush(hand):
    return 9
  if four_of_a_kind(hand):
    return 8
  if full_house(hand):
    return 7
  if flush(hand):
    return 6
  if straight(hand):
    return 5
  if three_of_a_kind(hand):
    return 4
  if two_pairs(hand):
    return 3
  if one_pair(hand):
    return 2
  return 1

cpt = 0
for line in f.readlines():
  hand1 = line.split(' ')[:5]
  hand2 = line.split(' ')[5:]
  hand2[-1] = hand2[-1][:-1]
  for k in range(len(hand1)):
    hand1[k] = [hand1[k][0],hand1[k][1]]
    hand2[k] = [hand2[k][0],hand2[k][1]]
  for k in range(5):
    if hand1[k][0] == 'T':
      hand1[k][0] = 10
    if hand1[k][0] == 'J':
      hand1[k][0] = 11
    if hand1[k][0] == 'Q':
      hand1[k][0] = 12
    if hand1[k][0] == 'K':
      hand1[k][0] = 13
    if hand1[k][0] == 'A':
      hand1[k][0] = 14
  for k in range(5):
    if hand2[k][0] == 'T':
      hand2[k][0] = 10
    if hand2[k][0] == 'J':
      hand2[k][0] = 11
    if hand2[k][0] == 'Q':
      hand2[k][0] = 12
    if hand2[k][0] == 'K':
      hand2[k][0] = 13
    if hand2[k][0] == 'A':
      hand2[k][0] = 14
  for k in range(5):
    hand1[k][0] = int(hand1[k][0])
    hand2[k][0] = int(hand2[k][0])

  if max_combin(hand1) > max_combin(hand2):
    cpt += 1
  if max_combin(hand1) == max_combin(hand2):
    if max_combin(hand1) == 2 and pair_egality(hand1,hand2) == 1:
      cpt += 1
    elif max_combin(hand1) == 1 and nothing_egality(hand1,hand2) == 1:
      cpt += 1
    else:
      print 'hello',hand1,hand2
print cpt
