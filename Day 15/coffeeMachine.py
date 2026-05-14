
userchoice = input("What do you want? (espresso/latte/cappuccino): ")
usermoney = int(input("How much money are you inserting? (in cents): "))
if(userchoice == "report"):
    print("Espresso: 150")
    print("Latte: 250")
    print("Cappuccino: 300")
    print(f"Money: {usermoney}")
if userchoice == "espresso":
    if usermoney < 150:
        print("Sorry, that's not enough money. Please insert at least 150 cents.")
    else:
        print("Here is your espresso. Enjoy!")
elif userchoice == "latte":
    if usermoney < 250:
        print("Sorry, that's not enough money. Please insert at least 250 cents.")
    else:
        print("Here is your latte. Enjoy!")
elif userchoice == "cappuccino":
    if usermoney < 300:
        print("Sorry, that's not enough money. Please insert at least 300 cents.")
    else:
        print("Here is your cappuccino. Enjoy!")
else:
    print("Sorry, we don't have that option. Please choose espresso, latte, or cappuccino.")
