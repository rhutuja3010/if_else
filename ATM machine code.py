card=input("enter the card")
if card=="ATM card":
    print("transaction in proceed")
    language=input("select the language")
    if language=="English" or "Hindi" or "Marathi":
       print("in process")
       pin=int(input("enter the pin"))
       if pin==4567:
           print("in process")
           account=input("enter the account type")
           if account=="saving" or "current":
               print("in process")
               transaction=input("enter the type of transaction")
               if transaction=="cash withdrawal":
                   print("in process")
                   amount=int(input("enter the amount"))
                   if amount<15000:
                       print("wait transaction in process")
                       print("collect the cash")
                       receipt=input("do you want receipt")
                       if receipt=="yes" or "no":
                           print("get receipt")
                           print("please collect the cash")
                           print("thank you")
                       else:
                           print("do not have cash")
                   else:
                       print("amount is not mention")
               else:
                   print("transaction is unsuccessfil")
           else:
              print("account is block")
       else:
          print("pin is wrong")
    else:
        print("panjabi")
else:
    print("pan card")
             
                        
        
           