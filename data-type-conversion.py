
# ================================ ~ DATA TYPE CONVERSIONS OPERATIONS EXAMPLES ~ ================================== #

# -------------------------------------------------------------------------------------------------- #
#                    PYTHON DATA TYPES AND CASTING METHODS
# -------------------------------------------------------------------------------------------------- #

#                       EXPLICIT TYPE CONVERSION         IMPLICIT TYPE CONVERSION

#  string                        str()                      x = "string"
#  integer                       int()                      x = 1
#  decimal number                float()                    x = 1.5
#  list                          list()                     x = ["a","b","c"]
#  dictionary                    dict()                     x = {a: b}
#  tuple                         tuple()                    x = (a,b)


# -------------------------------------------------------------------------------------------------- #
#                   CONVERT STRING INTO A LIST
# -------------------------------------------------------------------------------------------------- #

chars = "Thisisastringintoalist"

# with list comprehension
chars = [i for i in chars]

print(chars)

# output >>
#    ['T', 'h', 'i', 's', 'i', 's', 'a', 's', 't', 'r', 'i', 'n', 'g', 'i', 'n', 't', 'o', 'a', 'l', 'i', 's', 't']

# -------------------------------------------------------------------------------------------------- #

# simple way using list() method
chars = list(chars)

print(chars)

# output >>
#    ['T', 'h', 'i', 's', 'i', 's', 'a', 's', 't', 'r', 'i', 'n', 'g', 'i', 'n', 't', 'o', 'a', 'l', 'i', 's', 't']

# -------------------------------------------------------------------------------------------------- #

# with list slicing
word = "cabbage"
n = []
n[:0] = word
print(n)

# output >>

# ['c', 'a', 'b', 'b', 'a', 'g', 'e']

# -------------------------------------------------------------------------------------------------- #

# using split() method, to split string to list by word, not chars
word = "cabbage smells like cabbage"
print(word.split())

# output >>
#   ['cabbage', 'smells', 'like', 'cabbage']



# -------------------------------------------------------------------------------------------------- #
#                    TURN A STRING INTO KEY VALUE SORTED DICTIONARY BY OCCURRENCE
# -------------------------------------------------------------------------------------------------- #

chars = "bbbaaabaaaa"

def longest_repetition(chars):
    letters_dict = {}
    for i in range(len(chars)):
        letters_dict[chars[i]] = chars.count(chars[i])
    return letters_dict


# output >>
#   {'b': 4, 'a': 7}


# -------------------------------------------------------------------------------------------------- #
#                   TURN STRING INTO DICT
# -------------------------------------------------------------------------------------------------- #

import string

letters = string.ascii_letters
alpha_dict = dict.fromkeys(letters, 0)

# output >>
#   {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
#   'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
#   'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
#   'z': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
#   'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0,
#   'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}


# -------------------------------------------------------------------------------------------------- #
#                   CONVERTING TWO LISTS TO A DICTIONARY
# -------------------------------------------------------------------------------------------------- #

test_keys = ["Rash", "Kil", "Varsha", "Rash"]
test_values = [1, 4, 5]

res = {}

for key in test_keys:
    for value in test_values:
        res[key] = value
        # remove() removes any repeating values from list
        test_values.remove(value)
        break

print(res)

# output >>
#   {'Rash': 1, 'Kil': 4, 'Varsha': 5}



# -------------------------------------------------------------------------------------------------- #
#                   CONVERSION OF LISTS TO A DICTIONARY USING LIST COMPREHENSION
# -------------------------------------------------------------------------------------------------- #

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
print(res)

# output >>
#   {'Rash': 1, 'Kil': 4, 'Varsha': 5}



# -------------------------------------------------------------------------------------------------- #
#                   CONVERSION OF LISTS TO A DICTIONARY USING ZIP() FUNCTION
# -------------------------------------------------------------------------------------------------- #

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

res = dict(zip(test_keys, test_values))

print(res)

# output >>
#   {'Rash': 1, 'Kil': 4, 'Varsha': 5}



# -------------------------------------------------------------------------------------------------- #
#                   CONVERSION OF A DICTIONARY TO LIST OF KEYS USING GET() METHOD
# -------------------------------------------------------------------------------------------------- #

# Description:
# Python dictionary method get() returns a value for the given key.
# If key is not available then returns default value None.

# Syntax:
# Following is the syntax for get() method −
#       dict.get(key, default = None)
#       here we will use 'key=' as parameter

s_dict = {'Alex': 1, 'Anna': 3, 'Barb': 3, 'Charlie': 2, 'Jim': 1, 'Peter': 2, 'Zoe': 3}
s_dict_key_list = sorted(s_dict, key=s_dict.get)

print(s_dict_key_list)

# output >>
#    ['Alex', 'Jim', 'Charlie', 'Peter', 'Anna', 'Barb', 'Zoe']



# -------------------------------------------------------------------------------------------------- #
#                   BINARY STRING TO TEXT STRING REPRESENTATION
# -------------------------------------------------------------------------------------------------- #


# convert binary items to integers, then integer to ascii letters, and join

bits = '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'


def decode_pass(bits):
    bits_ls = bits.split()
    bits_as_str = ""
    for bin_value in bits_ls:
        x = int(bin_value, 2)
        y = chr(x)
        bits_as_str += y
    return bits_as_str


# output >>
#   password123


    ## SHORT VERSION OF SAME FUNCTION

def decode_pass(bits):
    bits_as_str = "".join([chr(int(i, 2)) for i in bits.split()])
    return bits_as_str


















