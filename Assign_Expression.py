# walrus operator := = assigns values to variables as part of a larger expression

happy = True
print(happy := False)  # Output: False

# food = list()
# while True:
#     food = input("What food do you like? ")
#     if food == "quit":
#         break
#     food.append(food)

foods = list()
while (food := input("What food do you like? ")) != "quit":
    foods.append(food)

# Funtion to variables
#####################################

say = print

say = print
say("Whoa!")

# High Order Functions = functions that can take other functions as arguments
#                       1. accepts a function as an argument
#                       or
#                       2. returns a function


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello World")
    print(text)


hello(loud)  # Output: "HELLO WORLD" becasue loud function is passed as an argument


def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))  # Output: 5.0
