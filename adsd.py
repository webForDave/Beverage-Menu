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


#########################################################################################################
# MAIN FUNCTION: program entry point
# calls every other functions in program - for now
def main():
    sum = 0 # initializes a aariable to hold the total price for a user's order
    while True: # validity stuff
        try:
            user_item = get_user_item() # invokdes the get_user_item functions and stores it in a variable for later usage

            if type(user_item) != int: # checks if user item is not of type integer 
                return user_item # returns the string, in this case, "order cancelled"
            else:
                quantity = get_quantity()
                sum += user_item * quantity # assigns the sum variable a new value - user item multiplied by the quantity 
            
                question = input('Anything else? Y/N ').strip().title() # prompts the user for something else

                if question == 'N': # returns the sum value if user is satisfied with order
                    return f"Total price: ${sum}"
                elif question == 'Y': # reprompts the user for an additional oders if not satisfied
                    continue
                elif question not in ["Y", "N"]: # if user enters something else than a yes or no
                    return f"\nInvalid Input\nTotal price: ${sum}"
        except ValueError:
            continue

##########################################################################################################
# function: Gets an order from the user
# prints the list of menu in a sequential order 
# prompts the user for an order
# validates order
def get_user_item():
    while True: # user order validity check
        try:
            # .Prints the list of menu in a sequential order
            print("X- Cancel Order") # allows the user to cancel an order
            for index, value in menu.items(): # menu items is defined above 
                print(f"\t {index} - {value[0]} = ${value[1]}") # prints the number of an item, it's name and it's price

            # .Prompts the user for an item
            user_prompt = input("What is your order? ").strip().title() # converts the input into uppercase and trim whitespace(s)

            # .Actual vality check
            if user_prompt == "X": # if user enters x or X, based on the print from above
                return "Order cancelled" # stops the order program
            else:
                for index, value in menu.items(): # loops through the keys and values in menu 
                    if int(user_prompt) == index: # converts user prompt into an integer and checks if it equals the current index
                        return value[1] # returns the price of the current index
                    elif int(user_prompt) not in menu.keys(): # checks if the item entered is in the menu number
                        raise ValueError # raises a value error which is caught below
        # .Catch errors
        except ValueError:
            return "Not an item in menu" # stops the process if user doesn't enter an appropriate value - a number in the menu printed
        except KeyboardInterrupt:
            return "Cancelled with the keyboard" # breaks the program if user interupts with keyboard


#########################################################################################################
# function: Prompts the user for a quantity
# reprompts if quantity is invalid
def get_quantity():
    while True: # validity check
        try:
            quantity = int(input("Quantity? ").strip()) # prompts the user for a quantity and converts it into an integer

            if quantity < 1: # checks for only positive integer
                continue # starts the loops all over if user enters zero or a negative integer 
            else:
                return quantity
        except ValueError: # starts again if user enters a value not equal to an integer, eg. a sting or character
            continue
        except KeyboardInterrupt: # on instances where the user quits the program with the keyboard, breaks out
            break


#####################################
if __name__ == "__main__":
    print(main())
