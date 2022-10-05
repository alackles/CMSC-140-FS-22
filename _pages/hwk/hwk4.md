---
title: Homework 4
permalink: /hwk/hwk4/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

# Homework 4: Lists and Dicts


**Due:** Thursday 10/13 @ 9:50 AM

**Learning Objectives**

- **L1**: Basics
- **L4**: Style

The purpose of this homework is to get you to incorporate new data structures (lists and dictionaries) into the kinds of problems you have been doing for the last three weeks of the course. 

## Submission Guidelines

You will turn this homework to Canvas under **Homework 4**. 

You should submit your homework as separate files, one for each question. 

The first 3 files should `.py` files. The last files should be a `.pdf` or `.txt` file with a short response. 

You can name the files any way you want as long as it's clear which files correspond to which questions. 

Please remember to follow the [Collaboration Policy](https://alackles.github.io/CMSC-140-FS-22/syllabus/#collaboration-and-plagiarism) for all homework assignments.

## Homework Questions

### Q1: Indexing

Consider the following two lists:

```py
a = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12, 13, 14, 16, 15, 17, 18, 18]
b = list(range(20))
```

Write a function that takes in both lists and returns a list of all the indices where the lists differ. 

Example:

```py
diff = listdiff(a, b) # this shouldn't print anything
print(diff) # this should print [8, 15, 16, 19]
```

### Q2: Schedule Saver

Write a dictionary to store your own course schedule for this term. The **keys** should be the name of each course. The **values** should themselves be dictionaries with the following information as key-value pairs:

- Course name
- Professor(s) 
- Units 
- Meeting times _as a list_ (e.g. for this class `["M 9:50 - 11:00", "W 9:50 - 11:00", "R 10:25 - 12:10"]`)

Then, print out the information from this dictionary in the following format using `for` loops (here's my own schedule as an example):

```
Course Code: CMSC 140
- Course Name: Intro to Python
- Professor: Ackles
- Units: 6
- Meets:
  M 9:50 - 11:00
  W 9:50 - 11:00
  R 10:25 - 12:10
----
Course Code: CMSC 510
- Course Name: Data Structures and Algorithm Analysis
- Professor: Gregg, Ackles
- Units: 6
- Meets:
  M 3:10 - 4:20
  W 3:10 - 4:20 
  F 3:10 - 4:20
```

You should include the `---` between each individual course. I won't be super picky about spacing, except that each entry should be on its own line. 


### Q3: Our old friend Random Number Guesser

There's still more fun to be had with the random number guesser. 

Your random number guesser from last week should now be a function that takes in a number of guesses and then walks the user through that number of guesses, telling them when their guess is too high or too low and ending when they're out of guesses. 

Here is the new functionality you should add:

- Store the user's past guesses in a list
- When the guessing game ends (either in failure or success), print out the **average** of all of their guesses

### Q4: Good Guesses?

Does the average of a user's guesses compared to the actual answer tell you anything about how "good" of a guesser they are, or what their strategy is for guessing? Explain. 

Note that there isn't a "right" answer I'm looking for here, just your thoughts on what the average could tell us. 
