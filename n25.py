'''code to check given triangle is equitalretal, isosceles, scalene'''
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))


if side1 + side2 <= side3:
    print("Invalid Triangle! Sum of two sides must be greater than the third.")
elif side1 + side3 <= side2:
    print("Invalid Triangle! Sum of two sides must be greater than the third.")
elif side2 + side3 <= side1:
    print("Invalid Triangle! Sum of two sides must be greater than the third.")

else:
    if side1 == side2:
        if side2 == side3:
            print("It is an Equilateral Triangle.")
        else:
            print("It is an Isosceles Triangle.")
    elif side2 == side3:
        print("It is an Isosceles Triangle.")
    elif side1 == side3:
        print("It is an Isosceles Triangle.")
    else:
        print("It is a Scalene Triangle.")