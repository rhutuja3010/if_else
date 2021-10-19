# if False:  #"false"
#     if True:
#         print("56")
# if True :  #true 
#     if False:   # false
#         print("76")
# if True :  # true
#     if True: #  true
#         print("78")



current_year=2021
birth_year=int(input("enter the birth year"))
future_year=int(input("enter the future year"))
futureage=future_year-birth_year
age= birth_year-current_year
if current_year-birth_year>0:
    print("your future age is:",futureage)
elif current_year-birth_year>0:
    print("your age is :",age)
else:
    print("wrong age")


