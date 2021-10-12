
# ================================ ~ * STRING OPERATIONS EXAMPLES * ~ ================================== #

#                         ~~ STRING METHODS AND DEFINITIONS LIST AT BOTTOM OF PAGE ~~


# -------------------------------------------------------------------------------------------------- #
#                   ACCESS VALUE OF ELEMENTS IN STRING BY INDEX POSITION
#                    - IN FOR LOOP USING RANGE(LEN(STRING))
# -------------------------------------------------------------------------------------------------- #

this = "thisisit"


def find_out(this):
    for i in range(len(this)):
        print(this[i])


find_out(this)

# output >>
#   t
#   h
#   i
#   s
#   i
#   s
#   i
#   t


# ~ or ~


this = "this is another example"

def find_out(this):
    ls = []
    for i in range(len(this)):
        x = this[i].upper()
        ls.append(x)
    return "".join(ls)


print(find_out(this))

# output >>
#   THIS IS ANOTHER EXAMPLE


# one-liner version of the same block above
def find_out(this):
    return "".join([this[i].upper() for i in range(len(this))])


print(find_out(this))

# output >>
#   THIS IS ANOTHER EXAMPLE

# -------------------------------------------------------------------------------------------------- #
#                   ADD " " BREAKS BETWEEN SPECIFIC NUMBER OF POSITIONS THROUGHOUT STRING
# -------------------------------------------------------------------------------------------------- #


str = "pieceofstringfrompositionithroughpositioni+2"

# n represents chunk length of string between breaks
n = 3

#  s[i:i+3] means, "look for piece of string from position i through position i+n"
chunks = [str[i:i+n] for i in range(0, len(str), n)]

print(chunks)

# output >>
#   ['pie', 'ceo', 'fst', 'rin', 'gfr', 'omp', 'osi', 'tio', 'nit', 'hro', 'ugh', 'pos', 'iti', 'oni', '+2']


# -------------------------------------------------------------------------------------------------- #
#                   COUNT NUMBER OF OCCURRENCES OF CHARS IN A STRING
# -------------------------------------------------------------------------------------------------- #

chars = "aaaaaabbbbbbaabbbcccccc"

# prints number of times per char, but letters are repeated, unsorted
for i in chars:
    occurrences = chars.count(i)
    print(occurrences)



# -------------------------------------------------------------------------------------------------- #
#                   TURN INTO A SORTED DICTIONARY BY NUMBER OF OCCURRENCES OF CHARS
# -------------------------------------------------------------------------------------------------- #

chars = "aaaaaabbbbbbaabbbcccccc"

def longest_repetition(chars):
    letters_dict = {}
    for i in range(len(chars)):
        # assigning keys with their values to the empty letters_dict() with a for loop
        letters_dict[chars[i]] = chars.count(chars[i])
    return letters_dict


print(longest_repetition(chars))

# output >>
#   {'a': 8, 'b': 9, 'c': 6}


# -------------------------------------------------------------------------------------------------- #
#                   RETURN TUPLE OF CHAR WITH HIGHEST OCCURRENCE
# -------------------------------------------------------------------------------------------------- #

# same beginning as above
def longest_repetition(chars):
    letters_dict = {}
    for i in range(len(chars)):
        letters_dict[chars[i]] = chars.count(chars[i])

    # this step finds key value of char with highest occurrence,
    # the "[0]" at the end pulls the tuple from the list and returns just the tuple
    max_keys = [(key, value) for (key, value) in letters_dict.items() if value == max(letters_dict.values())][0]
    return max_keys


print(longest_repetition(chars))

# output >>
#   ('b', 9)


# -------------------------------------------------------------------------------------------------- #
#               REVERSE ORDER INDEX OF WORDS IN A STRING WITH LETTERS KEPT IN NATURAL ORDER
# -------------------------------------------------------------------------------------------------- #

sentence = "Coding is SO awesome"

def rev_sentence(sentence):
    # split the string into a list of words
    words = sentence.split()

    # reverse the word list index, then join back to string separated by spaces
    reverse_sentence = " ".join(reversed(words))

    return reverse_sentence


print(rev_sentence(sentence))

# output >>
#   awesome SO is Coding


# -------------------------------------------------------------------------------------------------- #
#               COUNT NUMBER OF OCCURRENCES OF A SUBSTRING IN A STRING
# -------------------------------------------------------------------------------------------------- #

string = "ABCDCDC"
sub_string = "CDC"


def count_substring(string, sub_string):
    string_size = len(string)
    substring_size = len(sub_string)
    count = 0
    for i in range(0, string_size - substring_size + 1):
        if string[i:i + substring_size] == sub_string:
            count += 1
    return count

# output >>
#	2


# -------------------------------------------------------------------------------------------------- #
#               CHECK IF STRING IS ISOGRAM (IF IT CONTAINS EVERY LETTER IN ALPHABET AT LEAST ONCE)
# -------------------------------------------------------------------------------------------------- #

string = "kijhbsdckjbnawohfiuwbcklsdajncbikwujcebfvkwrejnb"

def is_isogram(string):
    string = string.lower()
    ns = "".join(c for c in string if c.isalpha())
    return len(ns) == len(set(ns))

print(is_isogram(string))

#output >>
#   False



# -------------------------------------------------------------------------------------------------- #
#               STRIPPING SPECIAL CHARACTERS FROM STRING | NESTED FOR LOOPS WITH CONDITIONALS
# -------------------------------------------------------------------------------------------------- #

s = "that's a pie$ce o_f p#ie!"

def remove_chars(s):
    ls = []
    for word in s:
        for letter in word:
            if letter.isalpha() or letter == " ":
                ls.append(letter)
    return "".join(ls)


print(remove_chars(s))

# output >>
#   thats a piece of pie



# -------------------------------------------------------------------------------------------------- #
#               NESTED FOR LOOPS WITH CONDITIONALS AS LIST COMPREHENSION | (SAME AS ABOVE)
#               STRIPPING SPECIAL CHARACTERS FROM STRING
# -------------------------------------------------------------------------------------------------- #

s = "that's a pie$ce o_f p#ie!"

# one-liner version, nested with conditionals list comprehension:

def remove_chars(s):

    return "".join([letter for word in s for letter in word if letter.isalpha() or letter == " "])


print(remove_chars(s))

# output >>
#   thats a piece of pie


# -------------------------------------------------------------------------------------------------- #
#               PAIRING NUMBER OF OCCURRENCES WITH WORD IN STRING AND STRIPPING SPECIAL CHARACTERS
# -------------------------------------------------------------------------------------------------- #

import re
sentence = "pairing@@ number%^ of of() occurrences in string#$ string"

def count_words(sentence):
    str = re.findall(r"[a-zA-Z0-9]+(?:'\w+)?", sentence.lower())
    freq = [str.count(word) for word in str]
    return dict(zip(str, freq))

print(count_words(sentence))

# output >>
#   {'pairing': 1, 'number': 1, 'of': 2, 'occurrences': 1, 'in': 1, 'string': 2}


# -------------------------------------------------------------------------------------------------- #
#               SAME AS ABOVE BUT WITHOUT SPECIAL CHARS STRIPPED:
# -------------------------------------------------------------------------------------------------- #

def count_words(sentence):
    sentence = sentence.lower().split()
    freq = [sentence.count(word) for word in sentence]
    return dict(list(zip(sentence,freq)))

print(count_words(sentence))

# output >>
#   {'pairing@@': 1, 'number%^': 1, 'of': 1, 'of()': 1, 'occurrences': 1, 'in': 1, 'string#$': 1, 'string': 1}



# -------------------------------------------------------------------------------------------------- #
#               PYTHON STRING STARTSWITH() METHOD
# -------------------------------------------------------------------------------------------------- #

# returns bool if string starts with the chosen text

txt = "Hello, welcome to my world."
txt_begins_with = txt.startswith("Hello")

print(txt_begins_with)

# output >>
#   True



# -------------------------------------------------------------------------------------------------- #
#               REMOVE DUPLICATE WORDS FROM STRING
# -------------------------------------------------------------------------------------------------- #

s = "my cat is my cat fat"

def remove_duplicate_words(s):
    set_s = []
    s = s.split()
    for i in s:
        if i not in set_s:
            set_s.append(i)
    x = " ".join(set_s)
    return x

print(remove_duplicate_words(s))

# output >>
#   "my cat is fat"



# -------------------------------------------------------------------------------------------------- #
#               CONVERT PHRASE TO AN ACRONYM
# -------------------------------------------------------------------------------------------------- #

words = "Portable Network Graphics"

def abbreviate(words):
    return "".join([letter[0].upper() for letter in words.replace('-', ' ').replace('_', ' ').split()])

print(abbreviate(words))

# output >>
#   PNG



# -------------------------------------------------------------------------------------------------- #
#               PYTHON STRING METHODS
# -------------------------------------------------------------------------------------------------- #


# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	    Returns a centered string
# count()	    Returns the number of times a specified value occurs in a string
# encode()	    Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	    Searches the string for a specified value and returns the position of where it was found
# format()	    Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	    Searches the string for a specified value and returns the position of where it was found
# isalnum()	    Returns True if all characters in the string are alphanumeric
# isalpha()	    Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	    Returns True if all characters in the string are whitespaces
# istitle()	    Returns True if the string follows the rules of a title
# isupper()	    Returns True if all characters in the string are upper case
# join()	    Joins the elements of an iterable to the end of the string
# ljust()	    Returns a left justified version of the string
# lower()	    Converts a string into lower case
# lstrip()	    Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	    Returns a string where a specified value is replaced with a specified value
# rfind()	    Searches the string for a specified value and returns the last position of where it was found
# rindex()	    Searches the string for a specified value and returns the last position of where it was found
# rjust()	    Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	    Splits the string at the specified separator, and returns a list
# rstrip()	    Returns a right trim version of the string
# split()	    Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	    Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	    Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	    Converts a string into upper case
# zfill()	    Fills the string with a specified number of 0 values at the beginning























