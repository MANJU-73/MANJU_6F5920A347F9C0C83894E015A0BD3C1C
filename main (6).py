num=int(input("2004:"))
if(num%4==0 ) :
  if(num%100==0):
    if(num%400==0):
      print("%d is a lep year"%num)  
    else:
      print("%d is not"%num)
  else:
    print("%d ia a leap year"%num)
else:
  print("%d is not"%num)
  