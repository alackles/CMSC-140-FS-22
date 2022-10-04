---
title: Week 4 Day 1 - Lists
permalink: /lectures/wk4-lists/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

View the code for the class on Github [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk4-lists.py).
# Lists

One thing that will make our programs a lot more powerful is the ability to store multiple pieces of data in the same place. This will make it easier to access as well as easier to manipulate. In Python, the most common place to store multiple pieces of data is in a _list_.

There is a LOT you can do with lists in Python. We won't cover every functionality of lists today, just a few of the basics. We'll continue to build on our understanding of lists as the term goes on. 

## Lists and Indices

Creating a list is as simple as putting multiple values into square brackets, separated by commas.

```py
my_list = [1, 3, 5, 8, 3, 2]
print(my_list)
```

You can have lists of any type, and you can mix types. 

```py
my_mixed_list = [2, "green", 2.4, True]
print(my_mixed_list)
```

To get a single value out of a list, you use square brackets to indicate which element you want.

```py
a = my_list[1]
print(a)
```

Notice this evaluates to 3; this is because, like with ranges, lists are 0-indexed.

```py
b = my_list[0]
print(b)
```

You can also use negative indices in lists to count backwards, but these don't start from 0 (because negative 0 is 0)

```py
classes = ["CMSC", "MATH", "STAT", "BIOL", "ART", "MUS"]
print(classes[-1])
print(classes[-2])
```

Finally, if you want a chunk of a list, you can use list slices:

```py
print(classes[0:5])
print(classes[1:2])
```

You can also leave off the first or second number if you want everything to the end or everything from the start:

```py
print(classes[:2])
print(classes[2:])
```

Go to In-Class Exercise 1.

## Modifying Lists

You can modify lists by accessing them at particular indices. Here's an example.

```py
print(classes)
classes[0] = "PHYS"
print(classes)
```

You can even use one part of a list to modify another part.

```py
classes[1] = classes[0]
print(classes)
```

Go to Exericse 2.

## Concatenation and Loops

Lists can be concatenated, like strings:

```py
list_a = ['a','b','c']
list_b = ['x','y','z']
final_list = list_a + list_b
print(final_list)
```

You can use this to build up a list piece by piece:

```py
numbers = []
for i in range(5)
    numbers = numbers + [i]
    print(numbers)
```

Speaking of for loops, you can actually use a for loop over a list:

```py
for item in final_list:
    print(item)
```

Or something like this:

```py
nums = [1, 3, 4, 8]
for i in nums:
    a = i**2
    print("Square of", i, "is", i**2)
```

Go to Exercise 3.

## Methods on Lists

There are some things we want to do to lists directly without creating a new list. Two of the most common things we might want to do are add to a list and sort a list. 

```py
example_list = []
example_list.append(4)
print(example_list)
example_list.append(2)
example_list.append(1)
example_list.append(3)
```

Notice we don't assign it back to itself. That's because when we're using a method it's doing something directly to the list, as indicated by the `.`. Not all functions can be used as methods.

We might also want to sort a list:

```py
example_list.sort()
```

Which changes the list in-place. 

## In-Class Exercises

### Exercise 1

Write a list that contains the names of all the classes you're taking this term. Then print the second value in the list (not index 2!).

### Exercise 2

Take the same list from above, and replace intro Python with a fake class name. Any class you like. Maybe "Advanced Sleeping". 

### Exercise 3

Work thorugh the following at your tables:

1. Create a list of 20 random numbers between 1 and 100 using the `random` module. (Hint: You will also need a loop.)
2. Using that list, create a new list which consists of the square root of each of those numbers from the first list. 