# logical operaters (and, or, not) = used to check if two or more conditional statements are true
############################################################################################################################

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")

# the not operater reverses the boolean value of a condition

# if not(temp >= 0 and temp <= 30):
#     print("The temperature is good today!")
#     print("Go outside!")
# elif not(temp < 0 or temp > 30):
#     print("The temperature is bad today!")
#     print("Stay inside!")

# return statements = functions can send back a value after it has been done processing
############################################################################################################################


def cube(num):
    return num * num * num


print(cube(2))