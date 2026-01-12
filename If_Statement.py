# if statement = a block of code that will execute if the following condition is true
###############################################################################################

age = int(input("How old are you?: "))

if age >= 18:
    print("You are an adult!")
    print("You can vote!")
elif age < 0:
    print("You haven't been born yet!")
elif 18 > age > 12:
    print("You are a teen!")
    print("You are close to vote!")
else:
    print("You are a child!")
    print("You will grow up soon!")
