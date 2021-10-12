
# ================================ ~ * DICTIONARY OPERATIONS EXAMPLES * ~ ================================== #


# -------------------------------------------------------------------------------------------------- #
#                   PYTHON DICTIONARY METHODS
# -------------------------------------------------------------------------------------------------- #


# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary


# -------------------------------------------------------------------------------------------------- #
#                   ACCESSING ITEMS
# -------------------------------------------------------------------------------------------------- #

car_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car_dict["model"]

print(x)

# output >>
#   Mustang

# -------------------------------------------------------------------------------------------------- #

# or use get() method

y = car_dict.get("brand")

print(y)

# output >>
#   Ford



# -------------------------------------------------------------------------------------------------- #
#                   ACCESSING KEYS
# -------------------------------------------------------------------------------------------------- #

x = car_dict.keys()

print(x)

#output >>
#   dict_keys(['brand', 'model', 'year'])



# -------------------------------------------------------------------------------------------------- #
#                   ACCESSING VALUES
# -------------------------------------------------------------------------------------------------- #

x = car_dict.values()

print(x)

#output >>
#   dict_values(['Ford', 'Mustang', 1964])


# -------------------------------------------------------------------------------------------------- #
#                   ACCESSING KEY VALUE PAIRS - DICT.ITEMS()
# -------------------------------------------------------------------------------------------------- #

# The items() method will return each item in a dictionary, as tuples in a list.

x = car_dict.items()

print(x)

# output >>
#   dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])



# -------------------------------------------------------------------------------------------------- #
#                   CHECK TO SEE IF KEY EXISTS IN DICT()
# -------------------------------------------------------------------------------------------------- #

if "model" in car_dict:
    print("Yes, 'model' is a key in car_dict")

# output >>
#   Yes, 'model' is a key in car_dict




# -------------------------------------------------------------------------------------------------- #
#                   HOW TO ADD KEY:VALUE TO A DICT (AS A FUNCTION)
# -------------------------------------------------------------------------------------------------- #

dict_l = {}

def show_how(name, grade):
    dict_l[name] = grade

print(show_how("jon", 8))

# output >>
#   {'jon': 8}



# -------------------------------------------------------------------------------------------------- #
#                   HOW TO ADD KEY:VALUE TO A DICT (OOP SYNTAX)
# -------------------------------------------------------------------------------------------------- #

class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade

    def show_kids(self):
        for k, v in self.students.items():
            print(f"{k}:{v}")


school = School()
school.add_student("Trevor", grade=5)
school.show_kids()

# output >>
#   Trevor:5


# -------------------------------------------------------------------------------------------------- #
#                   DICTIONARY COMPREHENSION
# -------------------------------------------------------------------------------------------------- #

# standard formula for implementing dictionary comprehension:
# d = dict((new_key, new_value) for key, value in d.items() if conditional)

# Example - Filter the dictionary by removing all items with a value of greater than 1

d = {"a": 1, "b": 2, "c": 3}

d = dict((key, value) for key, value in d.items() if value <= 1)

print(d)

# output >>
#   {'a': 1}



# -------------------------------------------------------------------------------------------------- #
#                   DICTIONARY UNPACKING
# -------------------------------------------------------------------------------------------------- #

# "**" is used for unpacking multiple keyword args or "keys"
# "**kwargs" allows the function to take an undetermined amount of keyword arguments
# the keyword arguments are packed as a dictionary in key, value pairs

def named(**kwargs):
    print(kwargs)

named(name="Bob",age=40)

# output >>
#   {'name': 'Bob', 'age': 40}

# -------------------------------------------------------------------------------------------------- #

# example starting with a dict()
details = {"name": "Jon", "age": 40}

named(**details)

# output >>
#   {'name': 'Jon', 'age': 40}

# -------------------------------------------------------------------------------------------------- #

# *args denotes undetermined amount of arguments
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,2,3, name='Fred', age=30)

#output >>
#   (1, 2, 3)
# {'name': 'Fred', 'age': 30}



# -------------------------------------------------------------------------------------------------- #
#                   MERGING TWO DICTIONARIES
# -------------------------------------------------------------------------------------------------- #

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5}

d_merged = {**d1, **d2}

print(d_merged)

#output >>
#   {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}



# -------------------------------------------------------------------------------------------------- #
#                   RETURN STRING ITEMS CONTAINED IN A DICTIONARY WITH COUNT OF ITEMS AS TUPLES
# -------------------------------------------------------------------------------------------------- #

word = "baabaganoosh"

letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
              'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
              'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
              'z': 0}


def score(word):
    word_score = [(key, word.count(key)) for key, value in letters.items() if key in word]
    return word_score


print(score(word))

# output >>
#   [('a', 4), ('b', 2), ('g', 1), ('h', 1), ('o', 2), ('n', 1), ('s', 1)]



# -------------------------------------------------------------------------------------------------- #
#                   RETURNING DICTIONARY VALUES OF MATCHING STRING ITEMS
# -------------------------------------------------------------------------------------------------- #

word = "perogies"

l_dict = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
            "x": 8, "z": 10}

def score(word):
    word_score = [l_dict[i] for i in word if i in l_dict.keys()]
    return word_score


print(score(word))

# output >>
#   [3, 1, 1, 1, 2, 1, 1, 1]


# -------------------------------------------------------------------------------------------------- #
#                   SIMILAR EXAMPLE RUNNING STRING AGAINST DICTIONARY KEYS FOR VALUES RETURN
# -------------------------------------------------------------------------------------------------- #

dna_strand = "ACGTGGTCTTAA"

comp_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(dna_strand):
    # makes list replacing value for string item if the item has a match in dictionary keys
    # "".join() converts list of values back to string format
    # in this case, joined by "" to make string have no spaces
    return "".join([comp_dict[i] for i in dna_strand if i in comp_dict.keys()])


print(to_rna(dna_strand))

# output >>
#   UGCACCAGAAUU



# -------------------------------------------------------------------------------------------------- #
#                   WORKING WITH TUPLES AS DICTIONARY VALUES
# -------------------------------------------------------------------------------------------------- #

student = {"name":"Rolf", "grades": (89,90,93,78,90)}

def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))


# output >>
#   Rolf 88.0



# -------------------------------------------------------------------------------------------------- #
#                   CONVERTING TWO LISTS TO DICTIONARY
# -------------------------------------------------------------------------------------------------- #

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

res = {}

for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break


# output >>
#   {'Rash': 1, 'Kil': 4, 'Varsha': 5}



# -------------------------------------------------------------------------------------------------- #
#                   CONVERTING TWO LISTS TO DICTIONARY USING DICTIONARY COMPREHENSION
# -------------------------------------------------------------------------------------------------- #

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]


res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}


# output >>
#   {'Rash': 1, 'Kil': 4, 'Varsha': 5}



# -------------------------------------------------------------------------------------------------- #
#                   CONVERTING TWO LISTS TO DICTIONARY USING ZIP()
# -------------------------------------------------------------------------------------------------- #

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]


res = dict(zip(test_keys, test_values))


print(res)

# output >>
#   {'Rash': 1, 'Kil': 4, 'Varsha': 5}












