number = int(input("entre the number"))
number_a = (number%10)
number_b = (number//10)%10
number_c = (number//100)%10
reverse_number = (number_a * 100)+(number_b * 10)+(number_c * 1)
if number <= 1000:
    print(reverse_number)
else:
    print("it cant")

