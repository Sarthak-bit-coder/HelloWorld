# function = a block of code which only runs when it is called
################################################################################

import functools


def hello(name):  # to add parameters add parameter inside the parentheses
    print("Hello " + name)
    print("Have a nice day!")


hello("Sarthak")  # calling function with name "Sarthak" for variable name
hello("Alice")  # Using different variable name


my_name = "Bob"  # using a variable as an argument and is used as temporary variable inside function
hello(my_name)

# Can mix and match argument types


def full_name(first_name, last_name, age):
    print("Your full name is " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")


# both arguments as strings and last parameter is integer
full_name("John", "Doe", 21)


# nested function calls
############################################################################################################################

# num = input("Enter a number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# prints the absolute value of a number rounded to the nearest integer
print(round(abs(float(input("Enter a number: ")))))


# sort() method = used with lists
# sort() function = used with iterables
################################################################################

students = ["Sarthak", "Alice", "Bob", "Charlie"]
students.sort()  # sorts the list in alphabetical order
# student.sort(reverse=True)  # sorts the list in reverse alphabetical order

sorted_students = sorted(students)  # returns a new sorted list

for i in sorted_students:
    print(i)

student = [("Squidward", "F", 61),
           ("Sandy", "A", 32),
           ("Patrick", "D", 23),
           ("Mr. Krabs", "B", 45),
           ("Plankton", "C", 55)]


def grade(grades): return grades[1]


# sorts the list based on the second element in each tuple
student.sort(key=grade)

students_tuple = (("Squidward", "F", 61),
                  ("Sandy", "A", 32),
                  ("Patrick", "D", 23),
                  ("Mr. Krabs", "B", 45),
                  ("Plankton", "C", 55))

# sorts based on third element in each tuple
sorted_students = sorted(students_tuple, key=grade)

# map function = applies a function to each item in an iterable (list, tuple, etc.)

# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]


def to_euros(data): return (data[0], data[1]
                            * 0.82)  # converts dollar to euros
# converts euros to dollars
def to_dollars(data): return (data[0], data[1]/0.82)


# applies to_euros function to each item in store list
store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

# filter function = creates a list of elements for which a function returns true

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Ross", 20),
           ("Chandler", 21),
           ("Joey", 16)]


# checks if age is greater than or equal to 18
def age(data): return data[1] >= 18


# applies age function to each item in friends list
drinking_buddies = list(filter(age, friends))
