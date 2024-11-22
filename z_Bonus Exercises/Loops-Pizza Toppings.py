Toppings = ["Olives", "Pepperoni", "Chicken", "Ranch"]
print(Toppings)

while Toppings:
    user_input = str(input("Choose A Topping For Your Pizza: "))
    if user_input.lower() == "olives":
        print("You Chose Olives")
    user_input = str(input("Is That It?"))
    if user_input.lower() == "yes":
        print("Enjoy!")
        break
    elif user_input.lower() == "no":
         user_input = str(input("Choose A Topping For Your Pizza: "))
    if user_input.lower() == "pepperoni":
        print("You Chose Pepperoni")
    user_input = str(input("Is That It?"))
    if user_input.lower() == "yes":
        print("Enjoy!")
        break
    elif user_input.lower() == "no":
        user_input = str(input("Choose A Topping For Your Pizza: "))
    if user_input.lower() == "chicken":
        print("you Chose Chicken")
    user_input = str(input("Is That It?"))
    if user_input.lower() == "yes":
        print("Enjoy!")
        break
    elif user_input.lower() == "no":
        user_input = str(input("Choose A Topping For Your Pizza: "))
    if user_input.lower() == "ranch":
        print("You Chose Ranch")
    user_input = str(input("Is That It?"))
    if user_input.lower() == "yes":
        print("Enjoy!")
        break
    else:
        print("You've Added All The Toppings Available")
        break