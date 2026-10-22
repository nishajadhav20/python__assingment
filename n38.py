'''check whether student pass all subject or not'''

DSA=int(input("Enter the marks of DSA="))
DS=int(input("Enter the marks of DS ="))
DBMS=int(input("Enter the marksof DBMS ="))
SEPM=int(input("Enter the marks of SEPM ="))
BS=int(input("Enter the marks of BS ="))
PYTHON=int(input("Enter the marks PYTHON ="))

passing_marks = 35
if DSA >= passing_marks and DS >= passing_marks and DBMS >= passing_marks and SEPM >= passing_marks and BS >= passing_marks and PYTHON >= passing_marks:
         print("Congratulations ...! you passed all subject") 
else:
        print("you cannnot passed all subject")                         