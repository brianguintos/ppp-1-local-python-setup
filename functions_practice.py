# A function named hello() that prints a greeting to the user. 
# This function should accept no arguments and returns nothing.
def hello(user_name):
    print(f"Hello, {user_name}. How are you doing today?")

# A function named pack() that accepts three arguments, and returns
# a single list with the three arguments inside as list elements.
def pack(arg_0, arg_1, arg_2):
    return [arg_0, arg_1, arg_2]

# A function called eat_lunch(). This function should accept a list 
# of any length, and print out a series of strings that say 
# "First I eat __" (the first element of the list), and 
# "Next I eat ___" (for the following elements in the list). 
# If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.
def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty")
    else:
        for index in range(len(lunch_items)):
            if index == 0:
                print(f"First I eat {lunch_items[index]}")
            else:
                print(f"Then I eat {lunch_items[index]}")


hello("Brian")
print(pack("apples", "bananas", "fish"))
eat_lunch(pack("apples", "bananas", "fish"))