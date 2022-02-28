from recepies import pantry, recipes

#print(pantry)
#print(recipes)

#d = {str(index+1): meal for index, meal in enumerate(recipes)} #dictionary comprochension
#print(d)

display_dict2 = {}
for index, key in enumerate(recipes):
    display_dict2[str(index + 1)] = key

# print(empty.items()) # we print out our dictionary items in tuple with their keys and values


for i, k in recipes.items():
    print(f"{i}: {k}")

def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to the `data` dict."""
    # if item in data:
    #     data[item] += amount
    # else:
    #    data[item] = amount
    data[item] = data.setdefault(item, 0) + amount #same as line 21-24


# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item] # so we selected the value, which is a key in this dictonary, so we call it, to get
        # even more data, in this case the ingredients of the food
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0) # default is 0, if item doesnt exist, we get the dafault value
            print("its here")
            print(quantity_in_pantry)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)


#---------------------------------------------------------------------------------

recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("potatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
    ],
}

recipes_dict = {
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
}

# using tuples
for recipe, ingredients in recipes_tuple.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients:  # ingredients is a tuple
        print(ingredient, quantity, sep=', ')

print()

# using a dictionary
for recipe, ingredients in recipes_dict.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients.items():  # ingredients is a dict
        print(ingredient, quantity, sep=', ')

