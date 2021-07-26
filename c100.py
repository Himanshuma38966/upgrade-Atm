def atm():
    
    atm =input("enter card number")
    

    if (atm == "7654321"):

        cash =input("how much cash u want")
        ne =input("Thank You press 1 to know your bank balance press 2 to get out")
    if (ne =="1"):
        print("30000")
    if (ne =="2"):
        print("Thank you visit again")



    if (atm != "7654321"):
        print("invalid card number")   


#####the card number is 7654321
atm()