# exception = an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions

try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print("You can't divide by zero idiot!")
    print(e)
except ValueError as e:
    print(e)
    print("You can only divide numbers!")
except Exception as e:
    print(e)
    print("Something went wrong :/")
else:
    print(result)
finally:
    print("This will always execute no matter what!")
