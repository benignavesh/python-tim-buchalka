# Any variable with many string parameters is known as a tuple
#  t="a","b","C"
# print(t)
# print("a","b","c")  # Not a tuple
# print(("a","b","c"))

# IF we need to print tuples, we have to use brackets.

metallica = "Ride the lightning", "Metallica", 1984
print(metallica)
print(metallica[0])
# Tuples are immutable, and the values cannot be changed.
# metallica[0] = "Master of puppets"  This gives an error.
# But we can use any segment or element of the tuple.

# In lists we use [] and insert the element, in tuples we directly write the elements.

metallica2 = ["Ride the lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets" # Here the element can be modified.
print(metallica2)

# Tuples are useful over lists when we deal with dictionaries.
# In dictionaries, we can only use immutable objects, which can only be achieved by tuples.
# In python, the value is assigned from right to left of the assignment operator, al
a, b = 12, 13
a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))

# We can also unpack a tuple by assigning names to each of the elements
# We cannot unpack a list, which is not immutable.
title, artist, year = metallica
print(title) # title is assigned first element of the tuple
print(artist)
print(year)
# We cannot append any item to a tuple, like we did with a list, since a tuple is immutable.
# WE can include a tuple inside another tuple
# For eg.
imelda = "More Mayhem", "Imelda May", 2011,((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish"))
# we need to provide parenthesis to make sure we have 4 elements with 2 elements inside a single element
# Else we had 8 separate elements

print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
# We can even split up the inner tuple, by creating more names and expanding tracks such as track1, track2 etc.
# We can also store the tuple that is within another tuple, within a list.

imelda2 = "More Mayhem", "Imelda May", 2011,([(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish")])
# List that contains individual tuples.
# We can now use the append function to add more elements into the tuple which was earlier not possible.
