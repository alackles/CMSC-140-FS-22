---
title: Lab 3 - Revise & Resubmit
permalink: /labs/lab3/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

The purpose of this lab is to take some of the problems you've done for homeworks and rewrite them as functions in order to familiarize yourself with using functions as part of your code. 
 
You'll rewrite two of the problems from Homework 2 as functions. Then, you'll write a third function to choose which of those functions to call. 

## Questions

### Q1: Adding Up

Write a function that calculates the sum of every number between two numbers. When called, the function should return the sum. ***Note:** Don't call this function`sum()`; that is already a built-in function in Python. You can call it `fsum()` or `my_sum()` or something similar.

Here is some example output:

```
>>> a = fsum(10, 15)
>>> print(a)
75
```

### Q2: Counting Down

Write a function that takes in two numbers. The first number is the number to start from; the second number is the number to count down by. When called, the function should print the countdown, and don't output any numbers below 0. See below for example output:

```
>>> countdown(18, 3)
Countdown:
18
15
12
9
6
3
0
```

Another example, where the count down doesn't fit:

```
>>> countdown(18, 4)
Countdown:
18
14
10
6
2
```

### Q3: Putting it Together

Now, write a function that does the following:

1. Asks the user which of the above two functions they would like to call.
2. When they select their function, ask them for the appropriate input for each function.
3. Run the functions with their inputs and print the result.

Here is an example of what it should look like when this function is called. (I'll also demo it in class.) In this case, something the user types in will be indicated with `{}`.

```
>>> function_chooser()
Welcome to the function chooser. Please choose a function.
1 = Cumulative Sum
2 = Countdown
Your choice: {2}
Please enter a start number: {20}
Please enter a number to count by: {5}
20
15
10
5
0
```

### CHALLENGE: One-Line Functions

This challenge question doesn't count towards mastery credit, but is a way you to try new things if you're already familiar with some of this material. 

Both Q1 and Q2 can be written as single-line functions using only default python. 

For Q2, this requires concepts we haven't seen before in class (and won't really deeply into); look into list comprehension and the `join()` function. 

Here's an example of list comprehension in Python; see what this does:

```py
print([i*i for i in range(6)])
```

## Assessment

You should turn this entire lab in in a single `.py` file.

For **proficiency credit**, when run, your script should appropriately select a function to run, and should produce the correct outputs for each of those functions when given reasonable inputs.

For **mastery credit**, your script should do the above, but it should also print hlpeful prompts for the user to input appropriate information, and should not print or display any information that is not asked for in Q3. 