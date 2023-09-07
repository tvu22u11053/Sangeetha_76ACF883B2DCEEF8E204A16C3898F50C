def leapyear(year):
    if (year % 4 ==0 and year % 100!=0 or year % 400 ==0):
        return Ture
    else:
        return False
year=int(input("enter the year"))
if leapyear(year):
  print("{} is aleapyear".format(year))
else:
  print("{}is notleapyear".format(year)) 