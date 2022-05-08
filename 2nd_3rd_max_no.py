a=int(input("1st no :"))
b=int(input("2nd no :"))
c=int(input("3rd no :"))
if a>b and a>c:
    print(a, "is grater")
    if b>c:
        print(b,"is second grater")
    else:
        print(c,"id second grater")
elif b>a and b>c:
    print(b,"is grater")
    if a>c:
        print(a,"is second grater")
    else:
        print(c,"id second grater")
elif c>b and c>a:
    print(c, "is grater")
    if b>a:
        print(b,"is second grater")
    else:
        print(a,"id second grater")
else:
    print("error")


















