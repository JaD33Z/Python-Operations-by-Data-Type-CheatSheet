# Python-Operations-by-Data-Type-CheatSheet
A collection of code blocks, functions and one-liners used to efficiently access, modify, and manipulate data with Python. Categorized by data type.

This is a repo that I figure can eventually grow over time. We've all run into some similar kinds of obstacles on more than
one occasion when solving problems. Now remembering exactly how you accomplished it the last time is a tall order. Instead of solving the same problem twice, or searching around for your old code, you can keep a centralized place with your solutions for quick reference.
Or to use as a learning tool for a better understanding of certain concepts, with notes to explain how they work. A variety of functions to handle tricky data type manipulation, some of these can be very useful. 
Remembering the specific order of syntax for more advanced operations can also be quite tricky, so I've included some syntax formulas, for instance, list comprehensions with if/else/elif conditionals as an example. Then you can just fill in the template with the appropriate data. 

## Example syntax template for list comprehension: 
```

  new_list = [new_item for item in item_list if condition]

```

## List Comprehension With Nested For Loops And Multiple Conditionals Syntax:
```
  new_string = "".join([letter for word in s for letter in word if letter.isalpha() or letter == " "])

```
The operations are categorized by data type for ease of finding an appropriate solution. They are labeled and grouped into simple to understand efficient codeblocks that can be easily modified if need be and incorporated into more complex functions. 
If you would like to share any code from your bag of python tricks that you have found to be useful in your experience, please feel free to contribute! 
