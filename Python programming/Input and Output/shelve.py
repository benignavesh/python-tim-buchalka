#Shelve is a type of dictionary but rather than storing in the memory, a shelf stores in a file
# here keys are strings, unlike dictionaries where keys can be immutable objects such as tuples.
# All the methods used with dictionaries can be used in tuples.


import shelve
with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange citrus fruit"
    fruit['naspati'] = "a sweet, green citrus fruit"
    fruit['lime'] = "a sour, green citrus fruit"
    fruit['mosambi'] = "a sweet, green citrus fruit"
    print(fruit["orange"])
    print(fruit["lime"])