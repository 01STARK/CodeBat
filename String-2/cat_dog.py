def cat_dog(str):
  countcat = 0
  countdog = 0
  for i in range(len(str)-2):
    if str[i] == "c" and str[i+1]=="a" and str[i+2]=="t":
      countcat +=1
    if str[i] == "d" and str[i+1]=="o" and str[i+2]=="g":
      countdog +=1
  return countcat == countdog
