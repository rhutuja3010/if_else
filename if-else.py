held=int(input("number of classed held"))
attended=int(input("number of classed attended"))
present=attended*100%held
if present<=75:
    print("percentage of class attended is student is allowed to sit in exam")
else:
    print("you are not alloud to sit in exam")
    