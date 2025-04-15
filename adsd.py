#########################################################
# Beverage Menu
# Models a real world ordering system - for beverages.
# Users start the program and are prompted for an order, 
# ...reprompted if orders are invalid, 
# ...or cancelled if a service isn't required any longer
#########################################################


# list of beverages, with their numbers on the list and price.
menu = {
    1: ["Tea", 3], 
    2: ["Coffee", 3], 
    3: ["Shakes", 5], 
    4: ["Hot Chocolate", 7],
    5: ["Coca-Cola", 2],
}


# MAIN FUNCTION: program entry point
# calls every other functions in program - for now
def main():
    total_price = 0 
    while True: # validity stuff
        try:
            user_item = get_user_item() 

            if type(user_item) != int: 
                return user_item 
            else:
                quantity = get_quantity()
                total_price += user_item * quantity 
            
                question = input('Anything else? Y/N ').strip().title() 

                if question == 'N': 
                    return f"Total price: ${total_price:.2f}"
                elif question == 'Y': 
                    continue
                elif question not in ["Y", "N"]: 
                    return f"\nInvalid Input\nTotal price: ${total_price}"
        except ValueError:
            continue


# function: Gets an order from the user
# prints the list of menu in a sequential order 
# prompts the user for an order
# validates order
def get_user_item():
    while True: # user order validity check
        try:
            #.Display menu in a sequential order
            print("X- Cancel Order") 
            for index, value in menu.items(): 
                print(f"\t {index} - {value[0]} = ${value[1]}")

            #.
            user_prompt = input("What is your order? ").strip().title() 

            # .Actual validity check
            if user_prompt == "X": 
                return "Order cancelled" 
            elif int(user_prompt) in menu:
                return menu[int(user_prompt)][1]
            else:
                raise ValueError
            # else:
            #     for index, value in menu.items(): 
            #         if int(user_prompt) == index: 
            #             return value[1] 
        #.
        except ValueError:
            return "Not an item in menu"
        except KeyboardInterrupt:
            return "Cancelled with the keyboard" 


# function: Prompts the user for a quantity
# reprompts if quantity is invalid
def get_quantity():
    while True: # validity check
        try:
            quantity = int(input("Quantity? ").strip()) 

            if quantity < 1:
                continue 
            else:
                return quantity
        except ValueError: 
            continue
        except KeyboardInterrupt: 
            break


if __name__ == "__main__":
    print(main())
