'''code to check  result status using match case'''

result=int(input("Enter your result 1.pass/ 2.fail  = "))

match result:
    case 1:
        print("RESULT: PASS")
    case 2:
        print("RESULT: FAIL")
    case _:
        print("Invalid result:")        