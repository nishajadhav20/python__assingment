'''check traffic signal actions  using match case'''

signal= str(input("Enter the signal  ="))
match signal:

 case "red":
   print("Stop...! You can stop know")
 case "green":
    print(" Go...! You can go know")
 case "yellow":
  print(" Be ready....! You can go or stop")
 case _:
   print("Invalid signal..! Follow the signal rules")