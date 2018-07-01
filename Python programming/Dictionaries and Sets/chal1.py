# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.


# locations = { 0: "You are sitting in front of a laptop",
#               1: "You are standing in a road",
#               2: "You are at the top of a hill",
#               3: "You are in a building",
#               4: "You are in the valley",
#               5: "You are in a forest"}
# exits = [{"Q" : 0},
#          {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0}, # If we start from road
#          {"N": 5, "Q": 0}, # If we start from hill
#          {"W": 1, "Q":0}, # If we start from Building
#          {"N": 1, "W": 2, "Q": 0}, # If we start from Valley
#          {"W": 2, "S": 1, "Q": 0}] # If we want to Forest
# loc = 1
# while True:
#     # availableExits = ""
#     # for direction in exits[loc].keys():
#     #     availableExits += direction + " , "
#     # We can use the join() built in method instead of the aforementioned code.
#     availableExits = ",".join(exits[loc].keys())
#     print(locations[loc])
#
#     if loc == 0:
#         break
#     direction = input("Available exits are : " + availableExits + "").upper()
#     print()
#     if direction in exits[loc]:  # if direction is available
#         loc = exits[loc][direction] #to change the current position
#     else:
#         print("You cannot go in that direction")

# keys() is used to handle the number of locations. here it is fine with 5 locations,
# but as the number of locations increases, the sequential order
# of the locations becomes hectic and that's where keys come into action.

# ----------------------------------------------------------------------------------------------------------------------

locations = { 0: "You are sitting in front of a laptop",
              1: "You are standing in a road",
              2: "You are at the top of a hill",
              3: "You are in a building",
              4: "You are in the valley",
              5: "You are in a forest"}
exits = [{"Q" : 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0}, # If we start from road
         {"N": 5, "Q": 0}, # If we start from hill
         {"W": 1, "Q":0}, # If we start from Building
         {"N": 1, "W": 2, "Q": 0}, # If we start from Valley
         {"W": 2, "S": 1, "Q": 0}] # If we want to Forest
vocabulary = { "QUIT": "Q",
               "NORTH": "N",
               "SOUTH": "S",

}
loc = 1
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + " , "
    # We can use the join() built in method instead of the aforementioned code.
    availableExits = ",".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    direction = input("Available exits are : " + availableExits + "").upper()
    print()
# Parse the user input, using our vocabulary dictionary
    if len(direction)>1:
        for word in vocabulary:
            direction = vocabulary[word]
            break
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("Wrong direction")