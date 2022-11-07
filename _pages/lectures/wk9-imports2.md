---
title: Week 9 Day 1 - Importing Your Own Files
permalink: /lectures/wk9-imports2/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

# Lecture/Live-Code

Often in programming we find ourselves reusing old code for new purposes. Within a single file, we can re-use functions so we don't have to do the same thing over and over again. However, when you make a new file, you might find yourself copying and pasting 

Please note that this is different than actually creating your own _module_ in Python. That is a more involved process that is beyond the scope of this class, but a link to a guide on how to do so is here.

## A Simple Example

First, I'll make a folder to house all of the files we're working with today, since file structure is an important part of what we'll be talking about. 

Recall from a past homework where you found the difference of two lists.

Maybe you want to reuse this code for a different list comparison. One thing you could do is copy the code over into a new file, but instead of doing that, you can use an import statement:

```py
from filename import function
```

Where `filename` is the file name and `function` is the function name!

Example for the files we're going to use today

```py
from diffs import listdiff
```

Where `diffs.py` is the filename and `listdiff()` is the function.

## Relative and Absolute Imports 

Just like with pathing, you have to specify where your files are being imported from. Python can handle both _relative_ and _absolute_ pathing, but not very well. 

In theory, if you have a directory structure like this:

```
└── project
    ├── package1
    │   ├── module1.py
    │   └── module2.py
    └── package2
        ├── __init__.py
        ├── module3.py
        ├── module4.py
        └── subpackage1
            └── module5.py
```

Either of the following should work:

```py
# in package1/module1.py

from ..package2.module3 import function1
```

```py
# package1/module1.py

from project.package2.module3 import function1

```

But in practice, it really depends on your file structure, your development environment (i.e. VS Code) and whether you have your `__init__.py` properly set up for each package. 

Pathing in Python is quite arduous sometimes, especially if you are trying to import something from what's called a 'parent' directory. For this reason, it's usually best to just import from the same directory or from child directories.

Go to in-class exercise 1.


# In-Class Exercise

## Exercise 1

How would you import a function called `go-fish()` from the file `games.py` into `project.py` with this file structure?

```
class/
├─ notes1.py
├─ notes2.py
├─ homeworks/
│  ├─ homework1.py
│  ├─ homework2.py
├─ projects/
│  ├─ project.py
│  ├─ data/
│  ├─ games/
│  │  ├─ games.py
```

## Exercise 2

For one of your past homeworks, you wrote some code which took as its input a string and gave as its output the string in alternating case. 

Create a new script which:

1. Uses the function from that file via import 
2. Takes input repeatedly from the user via command line and repeats it back to them in alternating case, until the user types "stop"

"Stop" should be accepted with any capitalization. 
