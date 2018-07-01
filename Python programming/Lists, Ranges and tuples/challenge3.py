# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, "Pulling the Rug", "Psycho", "Mayhem", "Kentish Town Waltz"
# print(imelda)

album, artist, year, track1, track2, track3, track4 = imelda
print("Album : {}".format(album))
print("Artist : {}".format(artist))
print("Year : {}".format(year))
print("Song 1 : {}".format(track1) + " \t" + "Song 2 : {} ".format(track2) + "\t" + "Song 3 : {} ".format(track3) + "\t" + "Song 4 : {}".format(track4))