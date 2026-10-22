'''grade description using match case'''

Grade = str(input("Enter the grade ="))
match Grade.upper():
    case "A":
        print("Excellent performance")
    case " B":
        print("Good job..!")
    case "C":
        print("Good...Improvement need")
    case "D":
        print("passed..! need more efforts")
    case "E":
        print("Failed..!please seek assistance")
    case _:
        print("Invalid grade")
        