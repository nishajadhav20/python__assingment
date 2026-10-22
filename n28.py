'''code to calculate discount based on shopping amount'''

Amount=int(input("Enter a shopping amount  ="))

if Amount >=2000:
    print("The discount is 20%")
elif Amount >= 1500:
    print("The discount is 18%")
elif Amount >= 1000:
    print("The discount is 15%")
else:
    print("Sorrry no discount under 1000 rupees shopping:")