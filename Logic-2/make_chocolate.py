def make_chocolate(small, big, goal):
  if goal >= 5 * big:
    remainder = goal - (5 * big)
  else:
    remainder = goal % 5

  if small >= remainder:
    return remainder
  else:
    return -1