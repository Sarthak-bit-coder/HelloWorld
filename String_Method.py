name = "john"

# Demonstrating various string methods
print(len(name))
print(name.find("h"))
print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("h", "n"))
print(name*3)

# str.format() method = formats specified values in a string
############################################################################################################################

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))  # Creates some value
# Changes the order by using indexes
print("The {1} jumped over the {0}".format(item, animal))
print("The {animal} jumped over the {item}".format(
    animal="cow", item="moon"))  # Using keywords

text = "The {} jumped over the {}"
print(text.format(animal, item))  # Using variables to format

# sets a minimum width of 10 characters
print("Hello, my name is {:10}.".format("name"))
# left aligns the text within the specified width
print("Hello, my name is {:<10}.".format("name"))
# right aligns the text within the specified width
print("Hello, my name is {:>10}.".format("name"))
# center aligns the text within the specified width
print("Hello, my name is {:^10}.".format("name"))

number = 3.14159
number_1 = 1000

# limits the number of decimal places to 2 floaing point numbers
print("The number pi is {:.2f}.".format(number))
# adds comma as a thousands separator
print("The number is {:,}.".format(number_1))
print("The number is {:b}.".format(number_1))  # formats the number as binary
print("The number is {:o}.".format(number_1))  # formats the number
# formats the number as hexadecimal (uppercase)
print("The number is {:X}.".format(number_1))
# formats the number in scientific notation
print("The number is {:e}.".format(number_1))
