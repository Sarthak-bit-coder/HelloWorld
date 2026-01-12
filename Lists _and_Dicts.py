# lists = used to store multiple items in a single variable
#####################################################################

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"  # change "pizza" to "sushi"
food.append("ice cream")  # add "ice cream" to the end of the li
food.remove("hotdog")  # remove "hotdog" from the list
food.pop()  # remove the last item in the list
food.insert(0, "cake")  # insert "cake" at the beginning of the list
food.sort()  # sort the list in alphabetical order
food.clear()  # remove all items from the list

print(food[1])  # prints "sushi"

for x in food:
    print(x)


# 2d lists = list of lists
##############################

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food_2 = [drinks, dinner, dessert]

# first bracket changes the list, second bracket changes the item in that list
print(food_2[0][0])


# tuples = collection which is ordered and unchangeable used to group together related data
#########################################################################################################

student = ("Sarthak", 19, "male")

# counts how many times "Sarthak" appears in the tuple
print(student.count("Sarthak"))
print(student.index("male"))  # finds the index for the word "male"

for x in student:
    print(x)


# sets = collection which is unordered, unindexed. No duplicate values
################################################################################

# duplicate "knife" will be ignored
utensils = {"fork", "spoon", "knife", "knife", "knife"}
# duplicate "cup" will be ignored
dishes = {"bowl", "plate", "cup", "cup", "knife"}

utensils.add("napkin")  # add "napkin" to the set
utensils.remove("fork")  # remove "fork" from the set
utensils.clear()  # remove all items from the set
utensils.update(dishes)  # add items from dishes set to utensils set
dinner_table = utensils.union(dishes)  # combine utensils and dishes sets

print(utensils.difference(dishes))  # items in utensils but not in dishes
print(utensils.intersection(dishes))  # items in both utensils and dishes

# order is random
for x in utensils:
    print(x)


# dictionaries = a unordered, changeable & indexed collection of key:value pairs
# useful to store data values like a map, which unlike other data types that hold only a single value as an item
#########################################################################################################################

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})  # add key:value pair to the dictionary
# change value of key "USA" from "Washington DC" to "Las Vegas"
capitals.update({"USA": "Las Vegas"})
capitals.pop("China")  # remove key:value pair with key "China"
capitals.clear()  # remove all key:value pairs from the dictionary

print(capitals["India"])  # prints "New Delhi"
print(capitals.get("Germany"))  # prints if "Germany" is in the dictionary
print(capitals.keys())  # prints all the keys in the dictionary
print(capitals.values())  # prints all the values in the dictionary
print(capitals.items())  # prints all the key:value pairs in the dictionary

for key, value in capitals.items():
    print(key, value)
