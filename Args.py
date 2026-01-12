# Keywords arguments = arguments that are passed to a function with a key = value syntax.
# This allows you to pass arguments in any order, making the code more readable and maintainable.
############################################################################################################################

def hello(firstname, middlename, lastname):
    print("Hello " + firstname + " " + lastname)


# Output: Hello John The Great Doe
hello(lastname="Doe", firstname="John", middlename="The Great")

# *args = a parameter that will pack all arguments into a tuple
############################################################################################################################


def add(*args):  # Single Asterisk is important
    total = 0
    stuff = list(args)
    stuff[0] = 0
    for num in args:
        total += num
    return total


print(add(1, 2, 3, 4, 5, 6))          # Output: 21

# **kwargs = a parameter that will pack all arguments into a dictionary
############################################################################################################################


def hello(**kwargs):  # Double asterisks is important
    print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="John", middle="The Great", last="Doe")
