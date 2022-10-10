---
title: Week 5 Day 1 - Strings
permalink: /lectures/wk5-strings/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

# Strings

We've already learned a lot about strings; how we can add them together, how to convert strings to ints or int to strings, how to use them to print text to the console or to index values in a dictionary. 

Today's class is going to be focused on a few more specific string operations; things you can do to manipulate strings to get the text that you want. 

## Live Code/Lecture

### Escape Characters in Strings

Something you may have noticed at some point in your exploration of printing various messages is that since quotation marks denote where strings stop and start, it's difficult to put a quotation mark _inside_ a string. 

```py
ex_string = 'This won't work
```
There are a few solutions to this quotes-in-strings problem.

#### Method 1: Double vs. Single Quotes

You can use either double or single quotes for strings, and Python will only use that type of quote to note the beginning and end of the string. 

```py
double_quote = "This 'string' is okay."
single_quote = 'This "string" is okay too.'
```

If you wanted to include both double and single quotes, though, this won't work. 

#### Method 2: Escape Characters

A backslash `\` indicates to Python that you want it to type exactly that character, not the Python meaning of the character. This will work for double and single quotes inside strings.

```py
esc_double = "This is \"fine\" now."
esc_single = 'This string\'s formatting is okay."
```

And yes, you can escape a backslash with `\\`. 

This could also be annoying if you have a ton of characters to escape, though, so Python provides something called a _raw string_. 

#### Method 3: Raw Strings

```py
rawstring = r'This will print \' exactly as I say \"\"'
```

### Multiline Strings

Another thing you might want to do often is print multiple lines with a single string. This is different than just calling multiple print statements because these multi-line strings could be stored in a single variable if you wanted. 

You can either use triple quotation marks, which will ignore newlines, or you can use the `\n` escape character.

```py
trip_quotes = """This is a string
that can span multiple lines.
Cool!"""

newline = "This is a string\n with a newline"
```

You can use these triple quotes for multiline comments in Python (but to be honest, I typically don't.)

Go to In-Class Exercise 1. 

### Indexing and Slicing Strings

Strings basically work as if they were lists of characters. 

I'll use my own name here; you can use yours!

```py
name = "Acacia Lee Ackles"
print(name[0])
print(name[0:6])
print(name)
```

Slicing the string doesn't change it, just like slicing a list doesn't change it. You can store these values in a new string if you want, though. 

```py
firstname = name[0:6]
```

Unlike list, you can't change a part of a string by assigning a new character to it. 

### In and Not for strings

You can also use `in` and `not` for strings the same way you can for lists. 

```py
print(firstname in name)
print("Hello" in "Hello")
print("j" in "fox")
```

### Splitting Strings

You can also break apart strings in other ways, most commonly with `split()`. Whatever goes inside the `()` in split is what the string will get split on; by default, it'll be any whitespace. 

```py
splitname = name.split()
print(splitname)
```

You can then use a trick called multiple assignment to grab different pieces of the string, if you know how it'll split. It's similar to how you could do `for key, value in dict.items()`. 

```py
first, middle, last = name.split()
print(first)
print(middle)
print(last)
```

You can also pass in a character.

```py
newname = name.split('a')
print(newname)
```

Notice that whatever you split on gets deleted from the split string; it's used as a delimiter. 

### Joining Strings

The opposite of splitting is joining, and it's done in basically a reverse way. 

```py
my_list = ["hello", "python", "class"]
nospace = "".join(my_list)
space = " ".join(my_list)
```

Go to In-Class Exercise 2.

### Strings in Strings

We've been doing something like this so far:

```py
fruit = "apples"
num = 7
print("I have " + str(num) + " " + fruit + ".")
```

This works, but is quite long. There are two shortcuts you can use in Python; string inerpolation, and f-strings. 

```py
print("I have %s %s" % (num, fruit))
```

Or, for an even more readable experience

```py
print(f'I have {num} {fruit}.')
```

### String Methods

A few things you might want to do to strings:

`.upper` and `.lower`:

```py
newname = name.upper()
print(newname)
newname = name.lower()
print(newname)
```

`.isupper` and `.islower`
```py
if newname.isupper():
    print("We are shouting!".upper())
else:
    print("we are whispering")
```

This is really helpful for things like inputting text; remember our birthday checker? Now we can just convert text to lower and not worry about capitalization. 

```py
age = input("How old are you?": )
birthday = input("Did you have a birthday this year?:" )
birthyear = 2022 - age
if birthyear.lower() == "yes" or birthyear.lower() == "y":
    print(f"You were born in {birthyear}")
else:
    print(f"You were born in {birthyear - 1}")
```

### Whitespace Stripping

Another formatting thing you often want to do is take away all whitespace from a string. This will become more apparent next week when we talk about file I/O. 

```py
space_string = "      Hello!  "
print(space_string.lstrip())
print(space_string.rstrip())
print(space_string.strip())
```

Like `split()`, the strip commands can also take a string.

```py
cool_string = "ooooo Hello this is my string ooooooo"
print(cool_string.strip('o'))
```


## In-Class Exercises


### Exercise 1: Literal

Print the following text exactly in your console however you like, except that it should be a single string.  

```
Here's a string for you!
This \n is a newline command
that didn't actually do anything.
```

### Exercse 2: Split and Join

Put the following string into your file and replace all the whitespaces with dashes, then print the result. Make sure to properly deal with the backslashes in the string. 

```
C:\MyDocuments\Classes\Intro to Python\Week 5
```

Output:

```
C:\MyDocuments\Classes\Intro-to-Python\Week-5
```
