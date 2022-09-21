---
title: Week 2 Day 1 - For and While Loops
permalink: /lectures/wk2-loops/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

View the code for the class on Github [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk2-loops.py).
# Loops

You may have noticed our book is called _Automate the Boring Stuff with Python_. So far we haven't really seen how that's applicable; while we have definitely written some code to do some easy things for us, like check alphabetical ordering, it's not like that will help us much with doing the kinds of tasks usually described as _boring_. Such tasks are usually repetitive, like renaming a lot of files at once, converting a lot of values from one unit to another unit, or similar kinds of tasks you may have had to do by hand. 

To do that sort of task, we need to execute the same piece of code more than once. We do this using blocks called loops.

## Lecture/Live Coding

### while Loops

A `while` loop is a piece of code that looks structurally very similar to an `if` statement. 

Remember that `if` statements look something like this:

```py
classcode = "CMSC 140"
if classcode == "CMSC140":
    print("Welcome to Class!")
```

`while` loops are very similar:

```py
classcode = "CMSC 140"
while classcode == "CMSC 140":
    print("Welcome to Class!")
```

Notice here, however, that the code just keeps running. (Press `ctrl`+`C` to get out.)

This is because an if statement checks that somethin gis true once, and then at the end, just continues on through the program. 

```py
classcode = "CMSC 140"
if classcode == "CMSC140":
    print("Welcome to Class!")
print("The if statement is over.")
```

```py
classcode = "CMSC 140"
while classcode == "CMSC 140":
    print("Welcome to Class!")
print ("The while loop is over.")
```

Notice that even when we exit the while loop forcefully, the rest of the program doesn't run. That's because we intentionally crashed our program, rather than actually exiting the while loop. 

So if the while loop checks to see that a condition is true, and if it is true, it runs the loop again, how will we ever stop the loop? 

Remember that we can execute any code we want inside the while loop. This includes changing values to _make the statmeent untrue_. 

```py
classcode = "CMSC 140"
if classcode == "CMSC 140":
    print("Welcome to Class!")
    classcode = "CMSC 150"
print("The if statement is over.")
print("Class Code:", classcode)
```

```py
classcode = "CMSC 140"
while classcode == "CMSC 140":
    print("Welcome to Class!")
    classcode = "CMSC 150"
print("The while loop is over.")
print("Class Code:", classcode)
```

Now, these statements effectively do the same thing. So what is the use of a while loop? 

A more realistic example is code where we want to perform a task a certain number of times. We can use a while loop, and some code within the while loop, as a counter to do so. Here's an example, again comparing to an if statement.

```py
times_through = 0
if times_through < 5:
    times_through = times_through + 1
    print("This block has executed " + str(times_through) + " times.")
print("times_through:", times_through)
```

```py
times_through = 0
while times_through < 5:
    times_through = times_through + 1
    print("This block has executed " + str(times_through) + " times.")
print("times_through:", times_through)
```

Every loop, the code executes again. Here is an example of something you can do that's a little more typical of what you might want a while loop for. Maybe you want to cut a number in half and see how many times it takes to get to just 1 element. 

```py
num = 25
while num > 1:
    num = num//2 # what is this double slash?
    print("Number: ", num)
```

Go to In-Class Exercise 1 to practice expanding on this. 

### for Loops

`while` loops execute continuously while their condition is still true. This can be really helpful if you aren't sure how many times you want the program to execute, as in the case of the number halving loop. But sometimes, you do know how many times you want it to execute, like in our `times_through` loop. 

For cases like this, you can use a `for` loop, which executes once for every time you tell it to. 

Let's change our while loop to a for loop to see how that works. 

```py
for times_through in range(5):
    print("This block has executed " + str(times_through) + " times.")
print("times_through:", times_through)
```

That's the general structure of a `for` loop. The `range()` operator is pretty powerful, and your book goes into a little more detail on options for its arguments. Feel free to reference that for your homework and exercises. 

Here's an example of some mathematics you can do with a for loop. 

```py
for i in range(10):
    print(str(i) + " squared is " + str(i**2))
```

You could do this with a while loop too, but notice that it will be a little longer and maybe less obvious:

```py
i = 1
while i <= 10:
    print(str(i) + " squared is " + str(i**2))
    i += 1 # note this
```

Is there a way to turn this while loop into a for loop?

```py
num = 25
while num > 1:
    num = num//2 
    print("Number: ", num)
```

In general, anything you can do with a for loop you can do with a while loop, but the reverse isn't necessarily true. 

In-class exercise time!

By the way: it's fine if this is confusing! It's normal, in fact! Loops are probably the most confusing thing to wrap your head around when you first start programming, mostly because they are so different to how we usually think. But once you get more practice with them, it will start to feel like second nature. 

## In-Class Exercises

### Exercise 1

Expand the program we wrote here:

```py
num = 25
while num > 1:
    num = num//2 
    print("Number: ", num)
```

1. Allow the user to input their own number when they run the code. 
2. Add a variable `counter` that starts at 0 and counts how many times the loop executes. Print this counter along with the number. 

Bonus (if you happen to know it): What's this operation called? 

### Exercise 2

Write a loop that prints every even number from 0 to 1000. 

It is up to you to choose which kind of loop you want to use. 

It is also up to you to determine how to print the even numbers only! There are at least two ways to do so; if you finish with time left, I suggest trying out a new way. 

If you have no idea where to start with accessing only even numbers, you can expand the hints below.

<details>
<summary>Hints</summary>
The first way is provided by your book, discussing the functionalities of `range()`.<br><br>
The second way is by using the python operator %, called the modulo. Googling "python modulo" will get you to an explanation. 
</details>
