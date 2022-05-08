num1=int(input("entre the num1 :"))
num2=int(input("entre the num2 :"))
num3=int(input("entre the num3 :"))
if (num1>num2 and num1<num3) or (num1>num3 and num1<num2):
    print(num1," second grater")
elif (num2>num1 and num2<num3) or (num2>num3 and num2<num1):
    print(num2,"second grater")
else:
    print(num3," second grater")

