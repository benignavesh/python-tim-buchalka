fruit={"orange": "sweet, orange,"}
print(fruit)

veg={"spinach":"cool"}
print(veg)
fruit.update(veg) # dict_name.update(dict_name2) joins the elements of dict_name2 to dict_name
print(fruit)
# update function does not return anything.
# We cannot use print(fruit.update(veg)), since it returns none
# dict_name.copy(dict_name2) copies all the elements of dict_name2 to dict_name
