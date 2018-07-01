# for i in range(10):
#     print (" i is now {}".format(i))
i=0
# while i<10:
#     print("i is now {}".format(i))
#     i+=1
    # Till the condition becomes false the loop continues.
    # We have to initialize the value of i. THIS WAS NOT NEEDED IN FOR LOOP.
# Indentation matters a lot, counter must be indented for while loop to know the counter.
available_exits=["east","north east", "south"]
chosen_exit =""
while chosen_exit not in available_exits:
    chosen_exit= input("Please choose a direction")
    if chosen_exit=="quit":
        print("Game Over.")
        break # to move out of the while loop.
print("You got out of here.")