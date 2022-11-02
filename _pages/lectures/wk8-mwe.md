---
title: Week 8 Day 2 - Asking Good Questions
permalink: /lectures/wk8-mwe/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

# Lecture/Live Code

This class period is aimed at giving you some more experience with finding the answers to questions you may have about Python after you leave this class. 

## Finding Others' Solutions

There are numerous places online you might be able to look for help. One of the most popular resources is Stack Overflow, but forums specific to the language you're interested in could also be a good resource. 

It's perfectly acceptable to google questions when you're unsure of the ansewr. Let's use an example from a recent homework. Maybe you want to check if something is a string. A good way to do this might be

```
python check if variable is list
```

We find some documentation for `is_instance`, which is helpful! It tells us exactly what we want to know. 

However, we can also find a [Stack Overflow answer](https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python), which gives a little more information. By reading this answer carefully, we can learn a new way to _approach_ the problem, not just a way to solve the question we originally had.


## Asking for Help

Before posting anything on Stack Overflow yourself, you should read the [tour](https://stackoverflow.com/tour).
### Minimal Working Examples

A _minimal working example_ is a piece of code that can be copy-pasted into someone else's computer and run without issues (working) and does not contain any extraneous information (minimal). 

However, if it was running _truly_ without issues, then you would probably have a solution to whatever problem you're asking about. So in practice, "minimal working example" means "minimally broken example". 

Let's use one of our past homework problems as an example.

Say you wanted to ask someone for help on the string problem. You may have tested out your code like this:

```py
instring = "hello world"
teststring2 = "hello_world_"
teststring3 = " hello    world"
outstring = ""
string_list = teststring.split(" ")
for i in range(len(teststring3):
    print(i)
    if teststring3[i] == " ":
        break
    if i % 2:
        print(teststring3[i])
        outstring += instring[i].upper()
    else:
        print(teststring3[i])
        outstring += instring[i].lower()
print(outstring)
```

It's common to end up with something like this when you're trying to figure out why something won't quite work. But you really want to strip the problem down to as little as possible when you're trying to give it to someone else to look at.

An added bonus is that _sometimes_, trying to create a MWE leads to you solving the problem.

Here's an example of a good MWE for the above.


```py
teststring = "hello world"
outstring = ""
for i in range(len(teststring):
    if teststring3[i] == " ":
        break
    if i % 2:
        outstring += teststring[i].upper()
    else:
        outstring += teststring[i].lower()
print(outstring)
```

We've removed all extraneous print statement and unused variables, noticed some places where the code wasn't consistent, and now have a better example to show to someone if we're having problems.

Minimal working examples can also be helpful when you have data that contains some sensitive data, in which case you'll probably also want _toy data_ to show people.

### Toy Input and Output

Sometimes the problem isn't necessarily that your code has problems that you don't know how to solve. Sometimes you don't know how to approach the problem at all. In this case, you'll want to provide what's called _toy_ input and output. This is basically input that has a similar structure to your input and output, but is much smaller (usually copy-pastable) and easy to see what the answer is with human eyes.

Here's some toy input and output for our baseball data:

Input:

```
Team,Win,Loss
Astros,7,0
Bills,0,4
Cubs,2,2
```

Output:

```
Astros
```
