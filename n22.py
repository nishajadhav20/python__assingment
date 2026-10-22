'''code to check salary bonus based on year of services'''

year=int(input("Enter the year of services  ="))

if year >= 35:
    print("Salary bonus is 20000:")
elif year > 25:
     print("Salary bonus is 16000:")
else:
     print("Salary bonus is 10000:")