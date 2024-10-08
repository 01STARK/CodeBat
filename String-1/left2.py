def left2(str):
  if len(str)==2:
    return str
  else:
    front = str[:2]
    return str[2:]+front