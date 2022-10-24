---
title: Week 6 Day 2 - Basic File I/O
permalink: /lectures/wk6-basic-io/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

Time to start loading in outside data! We're going to be spending some time on this because it's something you'll have to do very often in day-to-day applications of programming. 

# Lecture/Live Code

Just as you can open a file on your computer, make some changes to it, and then save that file, you can do the same inside Python itself. 

There are three basic steps to doing so, and they're the same steps you use when you're doing things manually.

1. Open the file
2. Read something from and/or write something to the file
3. Close the file

## Working with Files 

### Opening Files 

You can open files in Python by calling the `open()` function, where the argument is the path to the file. 

As an example, create a file called `hello.txt` in the same folder as your current python script. Write some text in it; anything you want. Then, you can do the following:

```py
hello = open('hello.txt')
```

Now, if you print `hello`, what do you expect to be in there?


### Reading Files 

To read the contents of a file, we need to call another function called `.read()` or `.readlines()`, depending on how you want to save your file. 

```py
file_contents = hello.read()
file_contents_list = hello.readlines()
```

### Writing Files

To write to a file, we need to explicitly tell Python we want to be able to write to it. The reason for this is that by default, Python will open files in _read only_ mode to protect you from doing something you don't want to do. (Unlike most interfaces you're used to using, there's no "are you sure?" in Python; it will just do whatever you ask.)

You can either overwrite the file contents entirely, or append to them.

To append, you should open the file in append mode.

```py
hello = open('hello.txt', 'a')
hello.write("here's some new content")
```

To overwrite, you should open the file in write mode.

```py
hello = open('hello.txt', 'w')
hello.write("here's some new content")
```

You can still read in both of these modes.

### Closing Files

Finally, we need to make sure we close our file when our script ends. The reason for this is that when you run the script, if you don't close the file, it'll just keep hanging out in memory. This is okay when you're using a standalone script, but a very bad habit to get into for when you eventually want to start loading programs into other programs. 

So whenever you have an `open()`, make sure you also do a `close()`.

```py
hello.close()
```


### With Open 

It's extremely easy to forget to close the file. That's why most of the time what you'll want to use `with open()` instead. It's a code block that automatically closes the file as soon as the code block is finished executing. 

```py
with open("hello.txt", 'a') as f:
    file_content = f.readlines()
print(file_content)
```

Notice that outside the `with open` block, you can work with the contents as normal. 

Go to In-Class Exercise 1.

## Files Line-by-line

Often times, you'll have files that have some kind of data in them that you're interested in processing one line at a time. For example, maybe you collected some data for a sociology class comparing the temperature outside on a given day to the number of people you noticed wearing hats. Your data looks  something like this

```
temp hats
72 2
42 18
60 19
77 5
88 4
21 20
38 22
```

Now you want to plot temperature vs. hats and see if there's any correlation. 

First, we would want to make lists of each of the values. But how do we do that if we're reading a file line by line?

Remember that readlines() returns a list of strings where each string is a line in the file. 

Here's some code to do so:

```py
temps = []
hats = []
with open("hats.txt") as f:
    next(f) # this allows us to skip the first line, which is header text
    for line in f.readlines():
        t, h = line.split(" ")
        temps.append(t)
        hats.append(h)
```

To plot these now, we can use matplotlib's plot function, which when given two lists plots them as x and y coordinates.

```py
import matplotlib.pyplot as plt
plt.plot(temps, hats)
plt.show()
```

Go to in-class exercise 2.

# In-Class Exercises

## Exercise 1

These are some randomly generated names. 

Copy the following into a file on your computer called `names.txt`. 

Using Python's file handling methods:

1. Print out the names to the console, separated by newlines
2. Add your name to the end of the file

```
Kajetan Phan
Ameer Alexander
Woodrow Hill
Winnie Holding
Kathryn Stacey
Tyra Gilmour
Steve Markham
Grant Olson
Elowen Blair
Mcauley Duran
```

## Exercise 2

Download (or copy & paste into a file) [this text file](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/baseball.txt) containing the win-loss records of all the Major League Baseball teams for 2022 (sourced from [here](https://www.baseball-reference.com/leagues/majors/2022-standings.shtml)). 

Write a Python script to read in the information and output the name of the statistically best team; that is, the one with the highest ratio of Wins to Losses.