a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
operator=input("enter the operator")
if operator=="+":
    print("add",a+b)
elif operator=="-":
    print("sub",a-b)
elif operator=="*":
    print("miltiplication",a*b)
elif operator=="%":
    print("modulus",a%b)
else:
    print("wrong")