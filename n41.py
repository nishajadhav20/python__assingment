'''print week day using match case'''

day = int(input("Enter the day number =   "))
match day:
 case 1 :
  print("Monday")
 case 2 :
  print("Tuesday")
 case 3 :
  print("Wedsday")
 case 4:
  print("Thusday")
 case 5:
  print("Friday")
 case 6 :
  print("Saturday")
 case 7 :
  print("sunday")
 case _:
  print("Invalid number") 
  
