print("========================= Question No. 1 =========================")
# Shopping Cart

shopping_cart = ["headphones" , "charger" , "cable" , "laptops" , "keyboard"]

#append,insert at 1,pop,remove.Print after each step.
# Using append method
appended_result = shopping_cart.append("Mouse")
print("Shopping Cart using append :" , shopping_cart)
# Using insert method
inserted_result = shopping_cart.insert(1 , "Speakers")
print("Shopping Cart using insert at 1 :" , shopping_cart)
# Using pop method
popped_result = shopping_cart.pop()
print("Shopping Cart using pop :" , shopping_cart)
# Using remove method
removed_result = shopping_cart.remove("cable")
print("Shopping Cart using remove :" , shopping_cart)