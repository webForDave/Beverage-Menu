menu = {
    1: ["Tea", 6], 
    2: ["Coffee", 12], 
    3: ["Shakes", 9], 
    4: ["Hot Chocolate", 10]
}


def main():
    sum = 0
    while True:
        try:
            user_item = get_user_item()

            if type(user_item) == str:
                return user_item
            else:
                quantity = get_quantity()
                sum += user_item * quantity
            
            question = input('Anything else? Y/N ').strip().title()

            if question == 'N':
                return f"Total price: {sum}"
            elif question == 'Y' or question != 'Y':
                continue
        except ValueError:
            continue


def get_user_item():
    # print list of menu.
    # prompt user for an item in menu.
    # reprompt for invalid items.
    while True:
        try:
            # .
            for index, value in menu.items(): # menu items is defined above 
                print(f"{index} - {value[0]} = ${value[1]}")

            # .
            user_prompt = input("What is your order? ").strip().title()

            # .
            if user_prompt == "X":
                return "Order cancelled"
            else:
                for index, value in menu.items():
                    if int(user_prompt) == index:
                        return value[1]
        # .
        except ValueError:
            continue
        except KeyboardInterrupt:
            break

def get_quantity():
    # prompt user for quantity
    # reprompt if quantity is not an integer
    while True:
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
        except ValueError:
            break


if __name__ == "__main__":
    print(main())
