'''code to check grade based marks'''

marks=int(input("Enter the marks ="))
if marks>=95 and marks<=100:
    print("the grade is A")
elif marks>=75 and marks<=95:
    print("the grade is B")
elif marks>=45 and marks<=75:
    print("the grade is C")
else:
    print("failed")

