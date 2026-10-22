'''print month day using match case'''

month= str(input("Enter the month name = "))
match  month:
  case "jan" | "march" | "may " | "july" | "august" |"october"| "december":
    print("Month have 31 days:")
  case   "april" | "june" | "septeber" | "november":
    print("Month have 30 days:")
  case "february":
    print("Month have 28 as well 29 days")
  case _ :
    print("Invalid Month")
