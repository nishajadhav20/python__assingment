'''code for electricity bill based on  units comsumed'''

unit=int(input("Enter the units ="))

if unit >=40 and unit <= 50:
    print("the electricity bill is 1000:")
elif unit >= 30 and unit <= 40:
    print("The electricity bill is 800:")
elif unit >= 20 and unit <= 30:
    print("The electricity bill is 500:")
elif unit >= 10 and unit <= 20:
    print("The electricity bill is 300:")
elif unit >= 0 and unit <= 10:
    print("The electricity bill is 100:")
else:
    print("the electricity bill is 1200:")