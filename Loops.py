import time

# while loop = a statement that will execute a block of code if the following conditional is and remains true
# an infinite loop = a loop that will never end unless externally stopped
############################################################################################################################

name = None

while not name:
    name = input("Enter your name: ")

print("Hello " + name + " what a great day outside!")


# for loop = a statement that will execute a block of code a limited amount of times
# limited amount of times = when you know beforehand how many times you want to loop through a block of code
############################################################################################################################

for i in range(10):
    print(i)


for x in range(50, 100+1, 2):
    print(x)


for y in name:
    print(y)


for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")


# nested loops = a loop inside another loop

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


# loop control statements = change a loops execution from its normal sequence
############################################################################################################################

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
