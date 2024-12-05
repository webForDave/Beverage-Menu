# q=("a")
# g=("x")
# v=0
# b=0
# k=0
# z=0
# print("T For Tea")
# print("C For Coffee")
# print("S For Shakes")
# print("H For Hot Chocolate")
# print("X To End Order")
# while q!=g:
#     x=str(input("Whats Your Order ? ")).upper()
#     y=int(input("Quantity ? "))
#     if x==("T"):
#         z=6*y
#     elif x==("C"):
#         v=12*y
#     elif x==("S"):
#         b=9*y
#     elif x==("H"):
#         k=10*y
#     else:
#         print("N/A")
#     q=input(str("Anything Else ? ")).lower()
# n=z+v+b+k
# print("Total Price:",n)
    
    

def main():
    return get_quantity()

def get_user_item():
    # print list of menu.
    # prompt user for an item in menu.
    # if item is invalid, reprompt.
    while True:
        try:
            print("""
                  X - cancel order
                  T for Tea
                  C for Coffee
                  S for Shakes
                  H for Hot Chocolate
                """)
            user = input('What is your order? ').strip().title()

            if user == 'X':
                return 'Order cancelled.'
            elif user == 'T':
                return 6
            elif user == 'C':
                return 12
            elif user == 'S':
                return 9
            elif user == 'H':
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
            quantity = int(input('Quantity? ').strip())
            
            if quantity < 1:
                continue
            else:
                return quantity
        except ValueError:
            continue
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    print(main())