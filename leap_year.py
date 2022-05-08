# a=int(input("entre the number"))
# if a%4==0 or a%400==0 and a%100!=0:
#     print("year is leap year")
# else:
#     print("year is not leap year")





# a=int(input("enter the year: "))
# if a%100==0:
#     if a%400==0:
#         print("century year",a)
#     else:
#         print("not a leap year")
# else:
#     if a%4==0:
#         print("leap year",a)
#     else:
#         print("not a leap year") 


# a=int(input("nu1"))
# b=int(input("num2"))
# if a>b:
#     print(a,"grater")
# else:
#     print(b,"is grater")


number = int(input("entre the number"))
number_a = (number%10)
number_b = (number//10)%10
number_c = (number//100)%10
reverse_number = (number_a * 100)+(number_b * 10)+(number_c * 1)
if number <= 1000:
    print(reverse_number)
else:
    print("it cant")


