day=input("entre the day")
if day=="thursday": 
   print("holiday")
   place=input("entre the place")
   if place=="hospital":
       print("you take first permission from disco")
       disco=input("entre the permission from disco")
       if disco=="yes":
           print("you take permission from team_member")
           team_member=input("entre the second permission from team_member")
           if team_member=="yes":
               print("you can go but take proper precaution")
               precaution=input("entre the precaution")
               if precaution=="mask or sanitiser":
                   print("you can go safly")
                   print("you can come before 7'o clock")
               else:
                   print("you don't go because you don't have precaution")
           else:
               print("you don't go because team_member don't give permission")
       else: 
           print("you don't go because disco don't give permission")
   else:
        print("you don't go because hospital is close")
else:
    print("you don't go because holiday is cancelled")
                   
