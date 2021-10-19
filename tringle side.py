x=int(input("entre the side1: "))
y=int(input("entre the side2: "))
z=int(input("entre the side3: "))
if x+y>z:
    print("tringle is valid") 
elif x+z>y:
    print("tringle is not valid")
elif y+z>x:
    print("tringle is not valid")
else:
    print("small")
