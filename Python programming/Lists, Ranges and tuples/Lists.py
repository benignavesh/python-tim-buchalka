#count(x) is used to count the number of occurennce of x.
ipAddress = input("Please enter an IP address : ")
print(ipAddress.count("."))
parrot_list = ["non pinin", "red", "green", "blue"]
#state is a type of counter that denotes the current state of
# counter being executed.
for state in parrot_list:
    print("The parrot is :" + state)
# append is used to append a statement at the end.
parrot_list.append("White")
#--------------------------------------------------#
even = [2,4,6,8]
odd=[1,3,5,7]
num= even + odd
# We can add the elements of the array / list directly.

print(num)

# To make the array in ascending order or in a ordered manner, we use sort

num.sort()
print(num)
# We don't use num.sort() because we don't create another object
# as in Java but we call the numbers and then sort accordingly.


# We can use a built in method in Python, to return the sorted number.
print(sorted(num))

# sorted(num) and num.sort () both generates the same sorted list.


list_1 = []
list_2=list() # same as list_1 just a different way of writing
print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))
# Lists can be called with no parameters or with an empty arguement
if list_1==list_2:
    print("Lists are equal")


#list() function automatically creates a list of the entries or arguements
print(list("AVESH"))

even = [2,4,6,8]

another_even = even
another_even.sort(reverse=True)
print(even)
# Here, we have updated the variable another_even by reversing the list/array, but in Python the updated another_even
#  updates the variable even as well.
# We can confirm this by comparing both variables.

print(even is another_even) # If true, it should return True
# Hence, we need to create other list from another variable, another_even.
one_more=list(even)
print(one_more is even) # Here, the list has been given another memory, so one_more is pointing to another list.
# is is different from == since, is compares the address of the memory, whereas == compares element by element

num= [even, odd]
print(num)
# Here, num returns two lists, within a list.

for num_set in num:
    print(num_set) # Prints the set of numbers
    for value in num_set:
        print(value) # Prints the elements of each set.