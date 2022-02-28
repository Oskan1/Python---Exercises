products = [("Computer", 750),
            ("Monitor", 150),
            ("Keyboard", 50),
            ("Mouse", 40),
            ("Mouse Mat", 20),
            ("HDMI-Cable", 10)
            ]

# Much more efficient using OOP! For example make product & shopping_cart a class.
line = "=" * 50
thin_line = "-" * 50
shopping_cart = []


def print_menu() -> int:
    """Print the requested menu."""
    print("What would you like to do?")
    print("1. Exit store")
    print("2. View Shopping Cart")
    print("3. Go to product list")
    menu = get_menu_option(range(1, 4), input(": "))
    if menu == 1:
        print("{}\nYou have quit shopping! See you next time :-)".format(line))
        return 1
    elif menu == 2:
        print(line)
        if not shopping_cart:
            print("Your cart is empty!\n{}".format(line))
            return 2
        total_cart_price = 0
        for index, item in enumerate(shopping_cart):
            product, price, amount, total_price = item
            total_cart_price += total_price
            print("{}: {} - price: {} - amount: {} - total: {}"
                  .format(index + 1, product, price, amount, total_price))
        print(thin_line)
        print("Your cart total is: {}".format(total_cart_price))
        print(line)
        return 2
    elif menu == 3:
        print(line)
        for index, product in enumerate(products):
            item, price = product
            print("{}: {} - €{}"
                  .format(index + 1, item, price))
        print(thin_line)
        add_to_cart(get_menu_option(range(1, len(products) + 1), input("What product would you like?\n: ")))
        print(line)
        return 3


def get_menu_option(valid_range: range, user_in: str) -> int:
    """Get a valid menu option."""
    while True:
        if user_in.isnumeric():
            user_in = int(user_in)
            if user_in in valid_range:
                return user_in
        user_in = input("This is not a valid option! Please select a different one.\n: ")


def get_valid_amount(user_in: str) -> int:
    """Get a valid amount."""
    while True:
        if user_in.isnumeric():
            user_in = int(user_in)
            if user_in > 0:
                return user_in
        user_in = input("This is not a valid amount! Please re-enter\n: ")


def add_to_cart(user_in: int):
    """Add user specified product to cart."""
    product_id = user_in - 1
    amount = get_valid_amount(input("How many would you like?\n: "))
    for item in shopping_cart:
        if products[product_id][0] == item[0]:
            item[2] += amount
            item[3] = item[1] * item[2]
            break
    else:
        price = products[product_id][1]
        shopping_cart.append([products[product_id][0], price, amount, price * amount])


while print_menu() != 1:
    continue