---
title: Week 5 Day 1 - Regex
permalink: /lectures/wk5-regex/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---


Regular Expressions is a deep topic in computer science and in programming. Regex is not something I'm going to be able to teach you right off the bat! It's not something I always remember exactly how to do. But it's something I want to introduce you to so that when we start reading in strings from files next week, it'll be a tool in your toolbox. 

**I do not recommend using these lecture notes as a reference for regular expressions.** There are many, many, MANY better and more complete references out there, including the two linked below. 

Here's a link to [my favorite regex checker](https://regexr.com/), which is not Python-specific.

Here's a link to [another pretty good regex checker](https://regex101.com/), which you can set to be Python-specific.

For most use cases, there won't be any difference between the two.

# Live Code/Lecture

## Pattern Matching in Strings

Last class we talked briefly about how you could pattern-match something in a string. 

Here's an example of something you could do with that. Let's say you have a list of a bunch of emails. 

```py
emails = ['acacia.ackles@lawrence.edu',
    'scott.corry@lawrence.edu',
    'deanna.donohue@lawrence.edu',
    'mmore500@msu.edu',
    'elizabeth.k.sattler@lawrenc.edu'
```

You want to check whether all of them are valid Lawrence email addresses. 

What's one way we can do this with what we've learned so far about strings? 

_Leaving this out so I can fill it in during class, when people give their ideas. No looking ahead!_

Go to In-Class Exercise 1.

## Regex: General

Sometimes we want to match things in the middle of a string, as well as at the end. Or we might want to check something more nebulous than just a straightforward match; for example, we might want to see if it contains only numbers, letters, and a set of special characters, like a password field.

This is where _regular expressions_, or _regexes_, come in. 

A regex is basically a way of mathematically describing a pattern of text. 

### Wildcards

Let's use an example first. 

What do these strings all have in common?

```
apple
appliance
approval
apply
clapping
mapped
```

They all contain string `app`. We could use `is in` for this, but we can also use a regular expression. 

The regex for this is simply

```
app
```

Now, what if we only wanted to match those strings that did not _start_ with app, but contained it instead?

Again, we could use a combination of `is in` and `not .startswith()`, but a shorter way to do this is with the regular expression:

```
.+app
```

What does the .+ do? 

`.` means "any character". 

`+` means "one or more of the previous group".

So this is saying, we want at least one character to come before `app` in this string. 

What if we replace `+` with `*`?

`*` means "zero or more of the previous group". So since we can have zero or more characters before `app`, it goes back to matching all of the elements. 

Go to in-class exercise 2. 

### Alphabet Groups

We can be more specific, though; what if we want to match just alphabetic characters?

That is, what if we want to match these


```
clapping
mapped
```

And none of these?

```
apple
appliance
approval
apply
28283app
!kappa
```

We can do the following: 

```
[a-z]+app
```

Which matches anything between a and z in the brackets. The brackets are how it knows that you should consider them all together, and not literally look for "a-z".

If we wanted to include capitals in this search, we could do 

```
[A-Za-z]+app
```

And it would work the same way. 

We could do a similar thing for numerical values:

```
[0-9]
```

Matches any number. 

### This or That

Sometimes you want to check whether something is one of two different values. A good example of this might be when you're looking for text that has different spellings in different languages. Grey can be spelled with an `e` or an `a`, for example. 

A regex to match any instance of this would be:

```
gr(e|a)y
```

You use the pipe symbol `|`, similar to in a match/case. In many languages this operator is how `or` is implemented. 


### Shorthand

There's also a shorthand way to write digits only, since it's pretty common, which is `\d`.

You can also check for all alphanumeric characters with `\w`, for _word_. 

Finally, any whitespace can be matched with `\s`. 

### Optional

Another common thing you might want to do is say that a character is optional. Some websites, for example, have `https` at the beginning, and others have `http`. You could check this with:

```
^https?
```

This will match both. The carat at the beginning means 'start of line' when it's outside a bracket. 

## Using Regexes in Python

To use these regexes in Python, the process is pretty simple. First we have to import the regex module:

```py
import re
```

There are three basic parts to checking something with a regular expression. 

Let's use as an example the idea at the beginning of checking if someone has a valid Lawrence email address. 

### 1 - Compile the RegEx

First you have to tell Python what you want the regex to be, in regex terms. 

```py
email_regex = re.compile(r'[a-z\.]+@lawrence.edu')
```

### 2 - Check if it matches

Now, `email_regex` stores a piece of data that you can access to compare to a string. 

To check this match, try something like this:

```py
is_match = re.match(email_regex, "acacia.ackles@lawrence.edu")
print(is_match)
```

Now we can see how we can use this in a loop to check these emails. 

### 3 - Use the information somehow

```py
def email_checker(emails):
    for email in emails:
        if not re.search(email_regex, email):
            print(f"{email} is not a valid LU email!")
```

Go to In-Class Exercise 3 for some practice writing regexes.

## Other Features of the RE module

If there's time, here's a few additional features we'll cover:

- ignorecase: You can ignore the case of an entry with `re.IGNORECASE`, or passing `re.I` as an optional third argument ot `re.search()`.
- match: `re.match()` has the same syntax as `re.search()` but only searches the beginning of a string.
- findall: `re.findall()` has the same syntax as `re.search() but will return a list of matches instead of a True or False value.

# In-Class Exercises

## Exercise 1

Write a function, `isValidFile()`, that takes in a string and returns `True` if the file ends with `.py` or `.pdf`, and False otherwise. 

Your function should return True for these inputs:

```
q1.py
hwk.pdf
py.pdf
```

And False for these inputs:

```
q1.cpp
hwk.pdf.txt
py.txt
```

## Exercise 2

Write a regular expression that will match all of these words:

```
Clowns
Crowned
```

and none of these words:

```
Owner
Power
Coop
Sown
```

## Exercise 3

Revise your `isValidFile()` function to use regex instead. 

You should still check whether it ends with `.py` or `.pdf`, but now you should also make sure the part before `.py`/`.pdf` includes only numbers and letters. 