# Slicing = Creating a substring by extracting elements from another string
# index operator [] = Gives access to a sequence's element (str, list, tuples)
############################################################################################################################

name = "Sarthak Aggarwal"

first_name = name[0:7]  # Strings start at index 0
# The end index is not includes while the start index is included
print(first_name)


# If end index is left blank, it slices to the end of the string same with first
last_name = name[8:]
print(last_name)

# The third parameter is the step size which determines the increment between each index
funky_name = name[0:8:2]
print(funky_name)

reversed_name = name[::-1]  # This slices the string backwards
print(reversed_name)

website = "http://www.google.com"
website2 = "http://www.youtube.com"

slice = slice(11, -4)

print(website[slice])  # Using the slice() function to create a slice object
print(website2[slice])

# index operator [] = Gives access to a sequence's element (str, list, tuples)
