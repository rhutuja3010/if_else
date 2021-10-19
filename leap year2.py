a=int(input("enter the year: "))
if a%100==0:
    if a%400==0:
        print("century year",a)
    else:
        print("not a leap year")
else:
    if a%4==0:
        print("leap year",a)
    else:
        print("not a leap year")