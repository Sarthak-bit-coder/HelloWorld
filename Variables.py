# variables hold a value, and you can combine strings with the "+" operator
############################################################################################################################

x = "Hello"
print(x + ", " + input("What is you name??\n"))

# Use str() to convert other data types to an integer
age = input("What is your age?\n")
print("Your are "+str(age)+" years old.")

# floats can have decimal points
height = input("How tall are you?\n")
print("Your height is "+str(height)+" meters.")
print(type(height))

# booleans hold either a True or False value
human = True
print("Are you a human: " + str(human))
print(type(human))

# scope = the region that a variable is recognized
############################################################################################################################

name = "Bob"  # global scope variable


def display_name():
    name = "Alice"  # local scope variable
    print("Hello " + name)


display_name()
print(name)

# Python uses the LEGB rule to decide the order of variable scope:
# L = Local
# E = Enclosing
# G = Global
# B = Built-in
