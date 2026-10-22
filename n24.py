'''code to check exam result'''

percentage=int(input("Enter the percentage ="))

if percentage >=85:
    print("Result is distinction:")

elif percentage >= 70:
    print("Result is first class :")

elif percentage >=35: 
    print("Result is pass:")  

else:
    print("Result is fail :")