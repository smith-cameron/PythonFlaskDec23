
# _ Functions
# < a named block of code that we can execute to perform a specific task
# < we can run at any time and as many times as required

def function_name():
    # code body
    # to work here
    print("hello_world from inside the function code block")
    return "return anything from inside the function we like"

# x = function_name()
# print(x)

# _ Conditionals
# < if, elif, else (conditional statements)
# < Conditional statements allow us to run certain lines of code
    # < depending on whether certain conditions are met.
# < These statements control the flow of how our code is executed

def conditionals():
    x = 12
    if x > 50:
        print("bigger than 50")
    else:
        print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute

    x = 55
    if x > 10:
        print("bigger than 10")
    elif x > 50:
        print("bigger than 50")
    else:
        print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

    if x < 10:
        print("smaller than 10")
    # nothing happens, because the statement is false
# conditionals()

def conditions_with_params(num1=0, num2=0):
    print(f"input param num1: {num1}")
    print(f"input param num2: {num2}")
    if num1 > num2:
        print("if")
        print(f"{num1} bigger than {num2}")
    elif num1 < num2:
        print("elif")
        print(f"{num2} bigger than {num1}")
    else:
        print("else")
        print("they are equal")
# conditions_with_params(0)

# _ Lists
# < an ordered and mutable collection of items.
# < a comma-separated sequence of elements within square brackets
# < Element values can be anything - even more composite types
# < 0 base index

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
words = ["this", "is", "a", "list", "of", "strings"]
mash_up = ['string', 4.65, 3, True, "another_string", numbers]
#    0      1    2      3         4              5

# > Accessing Values:
def accessing_list_values():
    # * print(list_name[index])
    print(mash_up[3])

    # > Replacing values
    # * list_name[index] = new_value
    mash_up[3] = "no longer a bool"
    print(mash_up[3])
    print(mash_up)

    # > Store value temporarily
    # * temp = list_name[index]
    temp = mash_up[3]
    print(temp)
    mash_up[3] = False
    print(mash_up)
    print(temp)
    mash_up[2] = temp
    print(mash_up)

    # > Replace a value with another value
    # * list_name[index] = list_name[other_index]
    print(numbers)
    numbers[0] = numbers[2]
    print(numbers)

    # > Adding values to a list
    # * list_name.append(new_value)
    numbers.append(9)
    print(numbers)

    # > Removing values of a list
    # * list_name.pop()
    # * list_name.pop(0)
    numbers.pop()
    print(numbers)
    numbers.pop(4)
    print(numbers)

    # > Number of Elements
    # * print(len(list_name))
    print(len(numbers))
# accessing_list_values()

# ? List vs. Tuple
# < Lists are mutable, while tuples are immutable (cannot be changed once created).
# < Lists are defined with square brackets, and tuples use parentheses.

def tuple_stuff():
    my_tuple = ('this is a tuple', True, [1, 2, 3, 4, 5])
    print(my_tuple)
    my_list = ['this is a tuple', False, [1, 2, 3, 4, 5]]
    print(my_list)
    import sys
    # < tuple take less memory becasue they are immutable
    print("Byte size of the list:", sys.getsizeof(my_list))
    print("Byte size of the tuple:", sys.getsizeof(my_tuple))
# tuple_stuff()

# _ Loops
# < used to execute a block of code repeatedly as long as a certain condition is met.
# < Python supports two main types of loops: `for` loops and `while` loops

# > FOR IN
def for_in():
    for unicorn in mash_up:
        print(unicorn)
# for_in()

def nested_for_in():
    for unicorn in words:
        print(unicorn)
        for i in unicorn:
            print(i)
# nested_for_in()

# > FOR IN RANGE
# < ITERATOR, START, STOP/BOUNDARY, STEP (DEFINED HORIZONTALY)
def in_range():
    print(numbers)
    for i in range(0, len(numbers), 1):
        print(f"i: {i}")
        print(f"value: {numbers[i]}")
# in_range()

# > WHILE
# < ITERATOR, START, STOP/BOUNDARY, STEP (DEFINED VERTICALLY)
def while_loops():
    i = 10
    while (i <= 20):
        print(f"i: {i}")
        i += 1
# while_loops()
