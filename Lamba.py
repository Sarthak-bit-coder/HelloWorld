import functools

# lambda functions = functions written in 1 line using lambda keyword
#                    accepts any number of arguments, but only has one expression

# lambda parameters: expression


def double(x): return x * 2
def multiply(x, y): return x * y
def add(x, y, z): return x + y + z
def full_name(first, last): return first + " " + last


def age(age): return True if age >= 18 else False


# reduce function = applies a function to an iterable and reduces it to a single cumulative value
#                   performs function on first two elements and then continues to apply it to the result and the next element


letters = ["H", "E", "L", "L", "O"]
# combines all letters into a single word
word = functools.reduce(lambda x, y: x + y, letters)
print(word)  # Output: HELLO

factorial = [5, 4, 3, 2, 1]
# calculates the factorial of 5
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)  # Output: 120
