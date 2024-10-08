def parrot_trouble(talking, hour):
  if (0<=hour<7 or 20<hour<24) and talking:
    return True
  else:
    return False
