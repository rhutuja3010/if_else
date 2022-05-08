# 18.Write a python program to input marks of five subjects Physics, Chemistry,
# Biology, Mathematics and Computer. Calculate percentage and grade according to 
# following:Percentage >= 90% : Grade A
#             Percentage >= 80% : Grade B
#             Percentage >= 70% : Grade C
#             Percentage >= 60% : Grade D
#             Percentage >= 40% : Grade E
#             Percentage < 40% : Grade F

physics=int(input("enter the marks of physics :"))
chemistry=int(input("enter the marks of chemistry :"))
biology=int(input("enter the marks of biology :"))
mathematics=int(input("enter the marks of mathematic :"))
computer=int(input("enter the marks of computer :"))
total=physics+chemistry+biology+mathematics+computer
percentage=total/500*100
if percentage >= 90 :
    print(percentage,"% :A grade")
elif percentage >= 80 :
    print(percentage,"% :B grade")
elif percentage >= 70 :
    print(percentage,"% :C grade")
elif percentage >= 60 :
    print(percentage,"% :D grade")
elif percentage >= 40 :
    print(percentage,"% :E grade")
else:
    print(percentage,"% :f grade")

