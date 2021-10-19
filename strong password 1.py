alphabetes=input("entre the alphabetes")
if alphabetes>="a" or alphabetes<="z":
    print("this is alphabetes")
    characters=input("entre the characters")
    if characters=="@" or characters=="#" or characters=="!":
        print("this is characters")
        number=int(input("entre the number"))
        if number>=1:
            print(alphabetes+characters+str(number))
        else:
            print("this is not number")
    else:
        print("this is not character")
else:
    print("this is not alphabetes")