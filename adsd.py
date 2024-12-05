def main():
    sum = 0
    while True:
        try:
            user_item = get_user_item()

            if user_item == 'Order cancelled.':
                return 'Order cancelled.'
            else:
                quantity = get_quantity()
                sum += user_item * quantity
            
            question = input('Anything else? Y/N ').strip().title()

            if question == 'N':
                return f"Total price: {sum}"
            elif question == 'Y':
                print(sum)
                continue
        except ValueError:
            continue


def get_user_item():
    # print list of menu.
    # prompt user for an item in menu.
    # if item is invalid, reprompt.
    while True:
        try:
            print(
                """
                    X - cancel order
                    T for Tea
                    C for Coffee
                    S for Shakes
                    H for Hot Chocolate
                """
            )
            user = input("What is your order? ").strip().title()

            if user == "X":
                return "Order cancelled."
            elif user == "T":
                return 6
            elif user == "C":
                return 12
            elif user == "S":
                return 9
            elif user == "H":
                return 10
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
