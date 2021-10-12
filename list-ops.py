
# ================================ ~ * LIST OPERATIONS EXAMPLES * ~ ================================== #

#                         ~~ LIST METHODS AND DEFINITIONS AT BOTTOM OF PAGE ~~


# -------------------------------------------------------------------------------------------------- #
#               LIST COMPREHENSION WITH NESTED FOR LOOPS AND CONDITIONALS SYNTAX
# -------------------------------------------------------------------------------------------------- #

s = "that's a pie$ce o_f p#ie!"

# one-liner version, nested with conditionals list comprehension:

def remove_chars(s):

    return "".join([letter for word in s for letter in word if letter.isalpha() or letter == " "])


print(remove_chars(s))

# output >>
#   thats a piece of pie



# -------------------------------------------------------------------------------------------------- #
#               LIST COMPREHENSION SYNTAX EXAMPLES
# -------------------------------------------------------------------------------------------------- #

# formula used for list comprehension syntax:
# new_list = [new_item for item in item_list]

# example:
array = [1, 2, 3, 4, 5]

def double(array):
    return [i*2 for i in array]


print(double(array))

# output >>
#   [2, 4, 6, 8, 10]


# -------------------------------------------------------------------------------------------------- #
#               IF CONDITIONAL STATEMENT LIST COMPREHENSION SYNTAX
# -------------------------------------------------------------------------------------------------- #


# formula used for list comprehension with conditional statement syntax:
# new_list = [new_item for item in item_list if condition]

# example:
array = [1, 2, 3, 4, 5]

def double_even(array):
    return [i*2 for i in array if i % 2 == 0]


print(double_even(array))

# output >>
#   [4, 8]



# -------------------------------------------------------------------------------------------------- #
#               IF ELSE CONDITIONAL STATEMENT LIST COMPREHENSION SYNTAX
# -------------------------------------------------------------------------------------------------- #

# formula used for list comprehension with conditional IF ELSE statement syntax:
# x = [f(x) if condition else g(x) for x in sequence]

# example:
array = [1, 2, 3, 4, 5]

def double_even(array):
    return [i * 2 if i % 2 == 0 else i for i in array]


print(double_even(array))

# output >>
#   [1, 4, 3, 8, 5]



# -------------------------------------------------------------------------------------------------- #
#               ELIF CONDITIONAL STATEMENT LIST COMPREHENSION SYNTAX
# -------------------------------------------------------------------------------------------------- #

# formula used for list comprehension with conditional ELIF statement syntax:
# x = [f(x) if condition else g(x) if condition else p(x) for x in sequence]


array = [1, 2, 3, 4, 5]

def check_values(array):
    return ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in array]


print(check_values(array))

# output >>
#   ['yes', 'no', 'idle', 'idle', 'idle']



# -------------------------------------------------------------------------------------------------- #
#               SORTING AN ARRAY. SORT ODD NUMBERS IN ASCENDING ORDER,
#               LEAVE EVEN NUMBERS IN THEIR ORIGINAL POSITIONS
# -------------------------------------------------------------------------------------------------- #

source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def sort_array(source_array):
    odds = iter(sorted(item for item in source_array if item % 2))
    return [next(odds) if i % 2 else i for i in source_array]


print(sort_array(source_array))

#  output >>
#   [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


# # iter(object, sentinel) =  creates an object which can be iterated one element at a time.
# # object - object whose iterator has to be created (can be sets, tuples, etc.)
# # sentinel -  (optional) - special value that is used to represent the end of a sequence

vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

print(next(vowels_iter))    # 'a'
print(next(vowels_iter))    # 'e'
print(next(vowels_iter))    # 'i'
print(next(vowels_iter))    # 'o'
print(next(vowels_iter))    # 'u'

# output >>
#    a
#    e
#    i
#    o
#    u



# -------------------------------------------------------------------------------------------------- #
#               LIST SLICING
# -------------------------------------------------------------------------------------------------- #

# List-to-Slice[Start:Stop:Step]

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

# The key point to remember is that the :stop value represents the first value that is not in the selected slice. So, the difference between stop and start is the number of elements selected (if step is 1, the default).

# The other feature is that start or stop may be a negative number, which means it counts from the end of the array instead of the beginning. So:

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

# Similarly, step may be a negative number:

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed



# -------------------------------------------------------------------------------------------------- #
#               PYTHON BUILT IN METHODS FOR LISTS/ARRAYS
# -------------------------------------------------------------------------------------------------- #

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list





