---
title: Week 1 Day 2 - Variables
permalink: /lectures/wk1-vars/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---
# Variables, Numbers, and Strings

View the code for the class on GitHub [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk1-vars.py).
## Live Coding

### Python Interpreter

The Python interpreter is basically just running Python directly on your computer, rather than through a script. You can start it up by simply typing

```
python3
```
in your terminal window. 

We can play around in here by doing some math:

```py
>>> 14 * (1/2)
7
>>> 1111 + 2
1113
>>> (1 - 5) * 4
-12
```

Or by printing some values:

```py
>>> "hello"
'hello'
>>> "lawrence" + "university"
'lawrenceuniversity'
```

Notice there's no space. Why? How would we add one?

This is a simple way to interact with Python, but it's not the most common way.


### Python Scripts

Of course, sometimes you want to go back and edit something you did before. This is where scripts come in. 

All a Python script does is feed the lines to the interpreter one at a time so that you can edit them first and then run them. It's usually the most helpful way to write and run Python. 

To create a Python script, all you have to do is name it with the `.py` extension. 

To run a Python script, navigate to the location of the script in your Command Prompt or Terminal (in VS code, you'll already be there) and type 

```
python {SCRIPTNAME}.py
```
where `{SCRIPTNAME}` is, of course, the name of your script.

We're going to make a script called `wk1-vars.py` where we do the rest of the problems today. 

### Variables

Let's go over some valid variable names: 

- Starts with a letter or underscore
- Can contain letters, numbers, and underscores

Conventions:

- snake_case 
- lowercase
- please don't make it a reserved word. your program won't be happy.

Tips:

- case matters
- Make your names as descriptive as possible without being annoying

### Data types

There are two very basic types of data in Python that we're interested in: Numbers and Strings.

#### Numbers

Numbers come in two basic formats: **integers** and **floating points**.

Integers are numbers without any decimals. E.g. `5`, `7`, `8`.

Floating point numbers, or floats, are numbers with decimal places. E.g. `5.4`, `2.0`, `-1.4`

In most languages, integers and floating point numbers are treated very differently. For example, dividing two integers will always produce an integer. In Python, this isn't the case. They act more like you usually assume numbers to act; they are interchangeable in most contexts. 

#### Strings

Strings are basically words or collections of words. 

Strings can have spaces:

```py
my_string = 'Python is cool'
```

Strings can have numbers:

```py
my_string = 'cmsc140`
```

Strings can even be added together (called _concatenation_). Note the space:

```py
my_string = 'hello ' + 'friend'
```

You can use either single or double quotes to note strings, but they have to match. If you want to put a single or double quote _inside_ a string, you can use an escape character like this:

```py
my_string = 'What\'s the temperature?`
```

This tells Python to interpret the apostrophe as a literal character, not a command.

### Interactions between Types

Try this yourself.

Can you add together an int and a float?

```py
num1 = 5
num2 = 4.2
num3 = num1 + num2
print(num3)
```

What about a float and a string? 

```py
apples = 20
sentence = "There are " + apples + "apples."
print(sentence)
```

Strings and integers don't add together because the operation `+` isn't well defined. The program isn't sure whether you want it to return a number or a sequence of letters, so it does neither.

### Conversions Between Type

In Python, it's easily possible to convert between types. For example, to change an integer or float into a string, simply use `str()`.

```python
my_variable = str(4.5)
print(my_variable)
```

It may seem initially as though nothing has changed. But try the following:

```py
apples = 20
sentence = "There are " + str(apples) + "apples."
print(sentence)
```

Now you're able to add them together, because you're being very clear about what you want.

What about something like this?

```py
apples = int("apples")
```

This kind of conversion isn't well-defined in Python. You could certainly create a conversion, but Python doesn't have one by default because it's not obvious what that would be. 

### Some Basic Functions

Here are some basic built-in functions that will help you complete various tasks:

User input can be handled by

```py
a = input()
print(a)
```

By default inputs come in as strings, even if they are numbers. 

As the program is executing, it will stop when it gets to an input line. But it won't tell you that by default, so it's important that you let the user know that that's why the program is idling. 

We have already used print a few itmes, but to be very explicit, you can do the following for pretty much any structure in Python. 

```py
my_list = [3, 4, 5]
print(my_list)
my_string = "My string!"
print(my_string)
my_dict = {1: "Hello", 2: ["another", "example"], 3: 4}
print(my_dict)
```

**This is one of the most popular and powerful features of Python.** In other languages you will often bang your head against the wall just getting something to print in a way that makes intuitive sense to you.

## In-Class Problems

### Problem 1: Birth Year

Write a Python script that does the following:

1. Create a variable called `cur_year` and set its value to `2022`.
2. Create a variable called `end_of_year_age` and set its value to whatever your age will be at the end of this calendar year.
3. Use those two variables (and any functions you need) to print out a sentence that tells you what year you were born. Example: `You were born in the year 1996`.

### Problem 2: Input/Output

Write a Python script that does the following:

1. When a user runs the program, ask for their name. Allow them to input it. 
2. Compliment them on their name, making sure to repeat it back to them. Example: `Hello, Caeli! That's a very nice name.`
3. Next, ask for their favorite number. Allow them to input it. 
4. Tell them the cube root of their favorite number (to at least 3 decimal places), making sure to repeat it back to them. Example: `The cube root of 15 is 2.466`.
5. Say goodbye.
   
### Problem 3: Challenge

If you have completed the previous two exercises easily, you probably know a little more Python than you are letting on.

Revise Problem 1 to ask the user if their birthday has already happened this year or not. Use that information to determine their birth year accurately. 