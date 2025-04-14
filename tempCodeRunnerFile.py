            if user == "X":
                return "Order cancelled."
            else:
                for index, value in menu.items():
                    if user == index:
                        user = value[1]
             