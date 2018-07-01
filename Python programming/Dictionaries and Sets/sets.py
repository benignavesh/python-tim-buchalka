# similar to dictionary, except that it supports unions and intersection.
# Same sets we use in set theory in maths
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animals in farm_animals:
    print(animals)
print("=" * 40)
wild_animals = set(["lion", "tiger", "panther", "elephant"])
print(wild_animals)

for animal in wild_animals:
    print(animal)
farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)
# We cant create an empty set, as that would create an empty dictionary
empty_set = set()
empty_set_2 = {}
empty_set.add("a") # Gives error since empty_Set 2 is a dictionary, and there is no .add function in dictionaries.
# empty_set_2.add("a")
even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print(len(even))
# print(len(squares))
# # modifications are only done to the current set, does not create a new set.
# print(even.union(squares)) # Prints all the elements of both the sets
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print(even.intersection(squares)) # prints all elements common to both the sets
#
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
#
# # We can also perform the difference and the addition of the sets
#
# print("even minus squares")
# print(sorted(even.difference(squares))) # we can use both methods of difference, but the .difference is more convenient.
# # This is because it clearly shows we are using difference method of sets.
# print(sorted(even-squares))
#
# print("squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares-even))

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("Symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

# The symmetric difference displays the same order of elements in both the cases.

# We can remove elements of a set by using two methods, discard and remove.

# remove gives an error when we try to delete an element which does not exist.
# discard does not give any error.

squares.discard(8) # does not give any error
# squares.remove(8) # Gives an error.

if 8 in squares:
    squares.remove(8)

# We can use the try-except to check the errors

# ==========================================

# We can also create or operate subsets or supersets in sets.

if squares.issubset(even):
    print("Square is a subset of even")
if even.issubset(squares):
    print("Even is a subset of squares")

# we have a frozen set which is immutable and cannot be tampered or updated.
