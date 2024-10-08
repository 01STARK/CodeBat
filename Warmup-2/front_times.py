def front_times(str, n):
  if len(str)>2:
    front = str[:3]
    return front*n
  else:
    return str*n