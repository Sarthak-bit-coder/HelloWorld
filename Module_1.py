# if __name_ == "_main_": = used to test code only when the module is run directly, not when imported

def hello():
    print("Hello World!")


if __name__ == "__main__":
    print("This code is being run directly")
else:
    print("This code is being imported from another module")

    # hello() function can still be used when imported
