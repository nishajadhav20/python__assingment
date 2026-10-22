'''check whwther the year is leep or century'''

year=int (input("enter the year:"))
if year%400==0:
    print(f"{year}is leep year or century year:")
elif year % 100 == 0:
    print(f"{year} is  century year but not leep year:")
elif year % 4 == 0:
    print(f"{year} is a leep year but not century year")
else:
    print("This is regular year")