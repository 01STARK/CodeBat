def lucky_sum(a, b, c):
  list=[a,b,c]
  s=0
  for i in range(len(list)):
    if list[i]!=13:
      s+=list[i]
    else:
      break
  return s