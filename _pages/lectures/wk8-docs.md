---
title: Week 8 Day 1 - Documentation & Errors
permalink: /lectures/wk8-docs/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

# Lecture/Live Code

[Code](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk8-docs.py)

There are two parts to today's class. First we'll talk about _documentation_, which is an extremely useful resource that any good programming language has which breaks down some of the 

## Documentation

You can explore Python's documentation [here](https://docs.python.org/3/index.html). In class, we'll walk through different components of this page together. 

Some things worth exploring here if you are out of class:

- "What's new in Python 3.11?"
- Library Reference
- Language Reference
- Skim through some of the FAQs

We're also going to specifically look at the _itertools_ module as an example. 

When you're done exploring, go to in-class exercise 1.

## Error Handling

Something we haven't talked about much in class yet is how to deal with input that isn't what we expect it to be. 

### assert Statements

Often if there's an error in our code, it's because we're assuming that a variable we've created has a different value than what it actually has. Here's an example. 

```py
x = list(range(20))
assert x[-1] == 20
```

This will give us an assertion error. It can be nice to include a message for such an error:

```py
x = list(range(20))
assert x[-1] == 20 , f"Expected 20, got {x[-1]}"
```

Go to in-class exercise 2.

You don't want to use assert statements for checking third-party user input, though; assert statements can be turned off and skipped over entirely, so this isn't good practice. For that, we instead use `try-except`.

### try-except Clauses

Try-Except is another way of handling errors. In this case, you would have to know what kind of errors you expect to see; however, a benefit of this construction is you can't turn it off, so the user could see your code, too.

```py
x = input("Please enter a number:")
try:
    x = int(x)
except TypeError:
    print("Not a recognizable number.")
```

You could also use this to try to open a file. 

```py
try:
    with open("baseball.txt") as f:
        print(line for line in f.readlines())
except:
    print("Something went wrong.")
```

There are two other keywords, _else_ and _finally_.

_Else_ will execute if no exception occured. _Finally_ will execute no matter what.

```py
try:
    with open("baseball.txt") as f:
        print(line for line in f.readlines())
except:
    print("Something went wrong.")
else:
    print("Nothing went wrong.")
finally:
    print("Done.")
```


# In-Class Exercises

## Exercise 1: Random

Find the Python documentation for the _random_ module. See if you can find a way to take the following list and return a new list with the same elements in a random order.

```py
subjects = ["English", "Math", "Science", "Humanities"]
```

## Exercise 2: Assertions

Paste the following code into your python script.

```py
orig_list = [2, 9, 20, 54]
new_list = orig_list
new_list[0] = 11
for x in orig_list:
    if x == 2:
        print(x)
```

It might not give you the output you're expecting. 

Try adding an `assert` statement before the `for` loop to check the first value of the original list. If the assert error fails, add a message to print out what `orig_list[0]` actually is. 



