'''code for blood donation eligiblity based on age nd weight'''

age = int(input("Enter the age ="))
weight = int(input("Enter the weight ="))

if age >= 18 and weight >= 50:
    print("Yes you can donate a blood:")
else:
    print("No sorry, you cannot donate a blood:")