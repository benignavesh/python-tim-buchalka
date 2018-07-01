menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage","bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage" , "spam"])
menu.append(["spam","egg", "spam" , "spam", "bacon", "spam"])
menu.append(["spam","egg", "sausage","spam"])
# print(menu)
# Now if we wish to search the entire list for those lists which do not have spam in them, we use for loop
for meal in menu: #meal is the counter and menu is the list
    if not "spam" in meal: # if we do not get spam in meal
        for value in meal:
            print(value) # prints the ingredients of the list.