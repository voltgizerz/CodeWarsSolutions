def points(games):
  sum = 0
  for i in range(len(games)) :
    games[i] = games[i].split(":")
    cmp = [ int(x) for x in games[i]]
    if cmp[0] > cmp[1]:
        sum+=3
    elif cmp[0] < cmp[1]:
        sum  = sum
    elif cmp[0] == cmp[1]:
        sum+=1
  return sum