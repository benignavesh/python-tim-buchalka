cities = {"Jaipur", "Ranchi", "Allahabad", "Delhi"}
with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

# A file named cities.txt is created and all the elements inside the list is copied in next lines.
# If the file does exist, it will be overridden.

# When we write a program to any external device, it first gets copied into the buffer, and then to the external device

cities = []
with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n')) # Appends all the elements of the city_file in cities[] list.
        # .strip('\n'is used to strip off all the \n from the elements of the list
print(cities)
for city in cities:
    print(city)

# strip is used to cut out some of the characters from the string, from the beginning, or from the end.
string1 = "Adelaide".strip('del')
print(string1)
# Here from del, since only de is found from the end, output gives "Adelai".


# Append is used to add any data, string etc to the end of the list, without altering the existing data.
