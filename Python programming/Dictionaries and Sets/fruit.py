fruit = {"Orange" : " a sweet, orangange, citrus fruit",
            "apple" : "good for making cider"}

print(fruit)
# print(fruit["Orange"])

# Here fruit is a dictionary which holds different fruits which further holds details regarding the fruits.

# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# The entry pear is added to the dictionary and the entire dictionary is printed.
# WE ARE NOT REMOVING OR REPLACING ANY ENTRY.
# fruit["pear"] = " very healthy"
# print(fruit)
# del fruit ["pear"]
# print(fruit) # del operation deletes the entire list from the dictionary.
# fruit.clear()
# print(fruit) # Clears the items from the list, different from delete.
# print(fruit["tomato"])
# while True:
#     dict_key = input("Enter a fruit : ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
    # We can print the statement inside the get argument.

    # if dict_key in fruit :
    #     description=fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("WE do not have a " +dict_key)
# # has_key is the replacement of dict_key in fruit.
#     fruit.has_key(dict_key)
#     print(description)
# for i in range (10):
#     for snack in fruit:
#         print(snack + "is" +fruit[snack])
#     print('-' * 40)
ordered_keys = list(fruit.keys())
ordered_keys.sort() # or ordered_keys = sorted(list(fruit.keys())
for f in ordered_keys:
    print(f + "-" + fruit[f])
    # In another simpler code, for f in sorted(fruit.keys()):
                                # print(' + "-" + fruit[f])
 # IMPORTANT
# --------------
# name_of_dictionary.keys() displays the key elements of the dictionary
# name_of_dictionary.values() displays the items inside the element
print(fruit.keys())
print(fruit.values())


fruit_keys = fruit.keys()
print(fruit_keys)

fruit ["Tomato"] = "not a good fruit"
print(fruit_keys) # Element tomato is added to the dictionary silently

# name_of_dict.items() displays all the items in the dictionary
# tuple(fruit.items()) is a built in method in python to display the items of the dictionary as a regular tuple.
# For eg.
f_tuple = tuple(fruit.items())
for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)
print(dict(f_tuple)) # dict() is a built in method to return back a dictionary from the tuple

