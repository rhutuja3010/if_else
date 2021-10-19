water=int(input("entre the water level"))
if water<1:
    print("fill the water")
elif water>=1 and water<10:
    print("do not fill watre")
elif water>10:
    print("it is overflow")
else:
     print("invalid")
    