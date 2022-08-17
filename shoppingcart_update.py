class Julia_shop():
    def __init__(self, items):
        self.items = items

    def menu(self):
        print("\n\n\nWelcome to Julia's shop. \n\tEnter the items you would like to purchase. \n\tEnter 'Show' to see your current list. \n\tEnter 'Delete' to remove a single item.\n\tEnter 'Clear' to empty your cart. \n\tEnter 'menu' to see the menu.\n\tEnter 'Finish' to finish adding items and proceed to check out.\n")
    
    def announcements(self):
        print("\n* * * * FIVE DOLLAR FRIDAY * * * * \nUse coupon code 'ALEXRULES' to get all items for $5. (regular price: $10)")

    def checkout(self):
        coupon = input("\n\tEnter the coupon code: ")
        if coupon.upper() == "ALEXRULES" or coupon.upper() == "ALEX RULES":
            price = 5
            print("\n\nCode applied!")
        else:
            price = 10
            print("\n\nCode invalid.")
        print(f"\nYour total today is ${len(self.items) * price}.00")
        reciept = input("\n\nWould you like a reciept? Enter Yes or No ")
        if reciept.lower() == "yes":
            print("\nRECIEPT FOR JULIA'S STORE:")
            for x in self.items:
                print(f"\t --- {x.title()} --- ${price}.00")
            print(f"\t --- TOTAL: --- ${len(self.items) * price}.00")

    def showitems(self):
        print("\n\tHere's your shopping cart so far:\n\t", end = "" )
        for x in self.items: 
            print(" -" + x.title(), end="")
        print("\n")    
          
    def clearitems(self):
        self.items = []

    def removeitems(self):
        removed_item = input("\n\tEnter the name of the item you'd like to remove: ")
        if removed_item.lower() in self.items:
            self.items.remove(removed_item.lower())
            print(f"\tOne {removed_item} removed from cart. Enter 'Delete' to remove more items or enter your next item.")
        else:
            print("sorry, we didn't understand your input. We are redirecting you back to the store.")

shopping_cart = Julia_shop([])

def go_shopping():
    shopping_cart.announcements()
    shopping_cart.menu()
    while True:
        item = input("\nEnter the name of the item you'd like to purchase:    ").lower()
        if item == "finish" or item == "quit":
            finish = input("\nThanks for shopping with us today! \n\tEnter 'Check Out' if are ready to check out. \n\tEnter 'Go Back' If you've changed your mind and want to continue adding items. \n\tEnter 'Quit' If you'd like to leave the store.\n\t").lower()
            if finish == 'go back' or finish == 'goback':
                print("sending you back to shop")
            elif finish == 'checkout' or finish == 'check out':
                shopping_cart.checkout()
                shopping_cart.clearitems()
                break
            elif finish == 'quit':
                print("\nWe hope next time you find something you like!")
                shopping_cart.clearitems()
                break
            else:
                print("Sorry, we don't understand that command. Please continue shopping")
        elif item == "show":
            shopping_cart.showitems()
        elif item == "delete" or item == "remove":
            shopping_cart.removeitems()
        elif item == "clear":
            shopping_cart.clearitems()
        elif item == "menu":
            shopping_cart.menu()
        else:
            quan = input(f"\tEnter quantity of {item}: ")
            if quan == '':
                shopping_cart.items.append(item)
            else: 
                for n in range(int(quan)):
                    shopping_cart.items.append(item)
    print("\n\n\nThank you for visiting our store! Have a great day!\n\n\n")
            
go_shopping() 




    

        
