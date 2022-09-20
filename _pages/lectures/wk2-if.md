---
title: Week 2 Day 1 - If/Else
permalink: /lectures/wk2-if/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

# If/Else and Match/Case

View the code for the class on Github [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk2-if.py).

So far we've been looking at simple evaluations and expressions in Python. In today's class we're going really start to get into _control flow_: how to make your program make choices. 

## Lecture/Live Coding

### Booleans

Boolean expressions are a type of expression in computer science. Just like an entity can be a number or a string, it can be a _boolean_. 

```py
my_num = 7 # a numeric value
my_string = "CMSC 140" # a string
my_bool = True # a boolean

```

Unlike numbers and strings though, which can take on an infinite number of values, booleans can only take on two values: `True` or `False`. 

This may not sound very useful, but it's really the key cornerstone of programming! Many, many, many times, you will be checking whether something is `True` or `False` and using that information to make choices in your program. 


### Boolean Operators 

Like numbers and strings, you can create booleans out of component pieces. Just like you can add 1 and 1 together and get 2, you can combine `True`s and `False`s to get new values. 

#### Operator "and"

The `and` operator evaluates to True only if both the things it connects are true. 

```py
print("T and T is:", True and True)
print("T and F is:", True and False)
print("F and T is:", False and True)
print ("F and F is:", False and False)
```

Notice that does not matter[^1] which order you put the expressions in. Just like addition and multiplication, `and` is symmetric. 

#### Operator "or"

The `or` operator evalutes to True if either of the things it connects are true.

```py
print("T or T is:", True or True) 
print("T or F is:", True or False)
print("F or T is:", False or True)
print ("F or F is:", False or False)
```

Like `and`, `or` is symmetric. 

#### Operator "not"

Finally, the `not` operator just flips the values of True and False.

```py
print("not True: " + str(not True))
print("not False: " + str(not False))
```

### Comparison Operators

One thing that makes booleans different from numbers and strings is that you can evaluate other kinds of data types _to_ a boolean. That is, you can check whether an entire expression is True or False, and then that expression will act like the value True or False. 

#### Equals and Not Equals

One example is the operators `==` and `!=`. These operators evaluate whether each side is equal to each other. They work on any value.

```py
45 == 45 # True
"hello" == "hello" # True
True == True # True
True == False # False
True != False # True
"hello" != "goodbye" # True
7 != 7 # False 
```

They also work on combinations of values

```py
7 + 4 == 11 # True
"hi" + "hi" == "hihi" # True
2 + 2 == 3 # False
1 + 1 != 4 # True
(True and False) == True # False
```

#### Greater Than/Equals

Another example is `>` and `>=`. `>` means something is strictly greater than; `>=` means something is greater than OR equals to.

Like `==` and `!=`, they work on expressions as well. They also work on all data types. For strings, they work based on alphabet

```py
7 > 5 # true
4 + 1 > 5 # false
5 >= 5 # true
"alphabet" < "balphabet" #true
"zebra" > "horse" #true
True > True # False
True >= True # True

```

#### Less Than/Equals

Works exactly the same way as greater than/equals.

```py
4 + 1 < 5  #false
4 + 1 <= 5 # true

```

## Truthy and Falsey Values

NOTE: numbers and strings will also evaluate to True or False _in the context of comparison operators_. `0` and empty strings will evaluate to `False`. Everything else will evaluate to `True`.

```py
print(7 and 5)
print("" and "string")
```

But they are NOT equal to True and False.

```py
print(7 == True) # false; they're not the same
print((7 and 5) == True) # true; the first expression evaluates to True, so the two are equal.  
```

Pause here to do exercise 1.

### Notes on Control Flow

Control flow is basically a term for things the program does that is not just reading and evaluating expressions as they are typed in. There is some input that triggers the evaluation of certain pieces of the code, called blocks.

This is powerful because it means the same code can be made to do many different things depending on the input, which makes it reusable for many more cases. 

In today's class we'll be looking at `if` statements and `match` statements. Both of these basically use the boolean value of something to decide whether or not to execute. 

### If Statements

`if` statements are lines of code with the following structure

```
if {statement is true}:
    {do something}
```

Here is a very basic example that will always execute:

```py
if True:
    print("Hello!")
```

Here is an example that will never execute:

```py
if False:
    print("Secret message that you won't see.")
```

Note that this is effectively no different than just writing `print("Hello")` in the first case, and writing nothing in the second case. So here is a more realistic example. 

```py
i = 0
if i == 0:
    print("i is equal to 0")
```

Anything you could do outside an `if` statement, you can do inside an `if` statement.

```py
i = 7
if i < 10:
    i = 10
    print(2 + 2)
    y = 25
    if 7 == 7:
        print("7 is 7")
print(i)
print(y)
```

### Else Clauses

You can choose to have your program do more than one thing based on the value of your if statement. 

You can add an `else` clause, which will only evaluate if the `if` clause is False. 

```py
example = 10
if example < 10:
    print("Small number.")
else:
    print("Big number.")
```

What will print if I change `<` to `<=`?

### Elif Clauses

You can similarly chain together these statements with `elif` to create a long chain of flow if there is more than one value you could take as input. 

```py
class_code = 140
if class_code == 140:
    print("This is Python Programming.")
elif class_code == 150:
    print("This is Java Programming.")
elif class_code == 270:
    print("This is Data Structures.")
elif class_code < 200: 
    print("This is a lower-level class.")
elif class_code >= 200:
    print("This is an upper-level class.")
elif class_code >= 400: 
    print("This is an advanced class.")
```

You can add an `else` clause at the end to catch all other cases, but this is not required. 

What will print if I set `class_code` to 500? 

It's now time for in-class problems. Work on exercise 2, and if you finish it, move on to exercise 3. 

## Match-Case

We'll only talk about this if we have a little time at the end of class.

Match-case is a relatively new construction in Python. I want you to know it exists, but it is VERY possible that you cannot use it if you don't have Python 3.10 (which, if you have Windows, you probably don't have 3.10). 

I'm going to show you how it works so you know it's out there, but you aren't going to be expected to use it on any homeworks or know how to use it. 

It works very similarly to `if-elif-else`:

```py
case_key = "cmsc"
match case_key:
    case "cmsc": 
        print("Computer Science")
    case "math":
        print("Mathematics")
    case _:
        print("Unrecognized.)

```

It can be a little more readable in certain situations.

```py
lo_mastery = 5
grade = ""

if lo_mastery == 7:
    grade = "A"
elif lo_mastery == 6 or lo_mastery == 5 or lo_mastery == 4:
    grade = "B"
elif lo_mastery <= 3 and lo_mastery > 0
    grade = "C"
else:
    grade = "D"

match lo_mastery:
    case 7:
        grade = "A"
    case 6 | 5 | 4:
        grade = "B"
    case 3 | 2 | 1:
        grade = "C"
    case _:
        grade = "D"
```

## In-Class Exercises

### Exercise 1: Booleans

1. Write an expression that uses `<` and evalutes to `True`.
2. Write an expression that uses `or` and `!=` and evalutes to `True`.
3.  Write an expression that uses `and`, `>=`, and `==` and evaluates to `False`.

### Exercise 2: If/Else

Write a program that asks a user to type their name. Tell them if their name comes earlier or later in the alphabet than your name. If you have the same name, tell them that as well!

Here is some scaffolding to get you started:

```py
user_name = input()
my_name = "Acacia"
# if their name is earlier than my name:
#   print a message
# ....
```

### Exercise 3: Write a Calculator

We're going to write a very simple caluclator in Python. This calculator takes two numbers from the user and asks them whether they want to add, multiply, divide, or subtract them. Then it performs the correct operation and prints the value. 

Below is what your program's output should be, including user input. It's up to you to write the internals!

```
Welcome to the calculator. 
Enter number 1: 8
Enter number 2: 4
Enter operation [a, s, d, m]: d
8 divided by 4 is 2.
```

-------

_Footnotes:_


[^1]: It _sort of_ matters. The expression on the left side of `and` will be evaluated first, so if it evaluates to `False`, the expression on the right will never be evaluated. This can be useful in certain specific cases where you are checking whether something is true that may be very computationally intensive. This won't come up in this class, but just in case you are curious about the finer details!