basic_salory = int(input("enter the salory"))
if basic_salory <= 10000:
    HRA = basic_salory * 20//100
    DA = basic_salory * 80//100
    print("gross salory1:",basic_salory + HRA + DA)
elif basic_salory <= 20000:
    HRA = basic_salory * 25//100
    DA = basic_salory * 90//100
    print("gross salory2",basic_salory + HRA + DA)
else:
    HRA = basic_salory * 30//100
    DA = basic_salory * 95//100
    print("gross salory3",basic_salory + HRA + DA)