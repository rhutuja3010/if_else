Day = input("entre the day")
if Day =="thursday":
    print("holiday you can go hospital")
    place = input("entre the place")
    if place == "hospital":
        print("you take first permission from disco") 
        disco = input("entre the permission from disco")
        if disco == "yes":
            print("you take second permission from team members")
            team_members = input("entre the permission from team members")
            if team_members == "yes":
                print("you can go to to hospital but with proper precaution")
                precaution = input("entre the precaution")
                if precaution=="mask or sanitiser":
                    print("you go to hospital safly")
                    print("you come in campus before 7 o'clock")
                else:
                    print("you not go beacuse you don't have precaution")           
            else:
                print("you don't go beacuse team members not give permission")
        else:
            print("you don't go beacuse disco not give permission")
    else:
        print("you can't go beacuse it is not hospital")
else:
    print("you can't go beacuse on this day not holiday")        