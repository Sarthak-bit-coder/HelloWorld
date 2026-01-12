import shutil
import os

path = "c:\\Users\\brijb\\Documents\\test.txt.txt"

if os.path.exists(path):  # Check if the file exists
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")

# Reading a file
###############################

try:
    with open("c:\\Users\\brijb\\Documents\\test.txt.txt") as file:
        print(file.read())  # Read the entire file content
#        print(file.closed)  # Check if the file is closed

except FileNotFoundError:
    print("That file was not found!")

# Writing to a file
###############################

text = "YOOOOOOOOOOOOOOOOOOOOOOOO\nThis is Brijesh here!\nHow are you?"
append_text = "\nThis is an appended line."

with open("c:\\Users\\brijb\\Documents\\text_writing.txt", 'a') as file:
    file.write(append_text)  # Append text to the file

# File copying
###############################

# copyfile() = Copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

shutil.copyfile("c:\\Users\\brijb\\Documents\\test.txt.txt",
                "c:\\Users\\brijb\\Documents\\test_copy.txt.txt")


# Moving a file
################################

source = "c:\\Users\\brijb\\Documents\\test_copy.txt.txt"
destination = "C:\\Users\\brijb\\Documents\\test_moved.txt.txt"

try:
    if os.path.exists(destination):
        print("A file already exists at the destination.")
except FileNotFoundError:
    print(source + " not found!")

# Deleting a file
################################
try:
    os.remove("c:\\Users\\brijb\\Documents\\test_moved.txt.txt")
#   os.rmdir  # Remove empty directory
#   shutil.rmtree  # Remove directory with all its contents
except FileNotFoundError:
    print("The file was not found, so it could not be deleted.")
except PermissionError:
    print("You do not have permission to delete that file.")
except OSError:
    print("You can only delete empty directories with os.rmdir().")
else:
    print("The file was deleted.")
