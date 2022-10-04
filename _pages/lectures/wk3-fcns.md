---
title: Week 3 Day 1 - Functions
permalink: /lectures/wk3-functions/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

View the code for the class on Github [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk3-fcns.py).
# Functions

Today's class is about building your own functions in order to use the same piece of code to perform different tasks. We did this a little bit with conditional statements (if/else) and with loops (both while and for), but recall how in those cases when we wanted a new input, we would have to go back and delete the old input to run the code again. Functions make code more re-usable. 

## Lecture/Live-Coding

### Built-in Functions

We have used functions before in Python. For example, `print()` is a function. `input()` is a function. 

Python has other built-in functions too which we haven't used as much; for example, `len()`, which takes the length of something:

```py
name_length = len("Acacia")
print(name_length)
```
You can also nest functions together:

```py
print(len("Acacia"))
```

and they execute from the inside outwards. 

Every time we call these functions, we can give them different inputs, and we don't have to delete the old inputs to do so. For example, we could do

```py
print("Hello.")
print("Goodbye.")
print(4)
print(7 == 3)
```

And it will just print everything out in a row. 

On the other hand, with what we've been doing so far, we'd have to either delete code or copy code to repeat it. For example:

```py
my_sum = 0
for i in range(1, 21):
    my_sum += i
print(my_sum)
```

if we wanted to change this to be in range 100, we'd either have to delete a part of it or copy the whole thing. But we can do better than that with a function! 

### Functions without Arguments

In Python, you define a function by the following structure.

```
def function_name(args):
    do something here
```

We can define a very simple function like this:

```py
def our_first_function():
    print("This is a function.")
    a = 7 + 2
    print(a)
```

If you run this code now, though, it won't do anything. That's because we've only _defined_ the function; to have it run, we need to _call_ it. 

Calling a function just means executing everything the function does.

We call functions by just typing their names. 

```py
our_first_function()
our_first_function()
```

Q: Why don't we need to wrap it in a `print()` function? 

### Functions with Arguments

You may have noticed that the function we wrote doesn't have anything in the parentheses, whereas functions like `print()` usually do. If we call `print()` with nothing in it, it will print exactly that: nothing.

We can create functions that take inputs and use them for their outputs. Here's an example. 

```py
def excited_print(my_string):
    print(my_string + "!!!!!!!")
excited_print("Hello")
```
Anywhere that the argument shows up inside the function, it will be replaced with whatever value you put into it.

However, if we try to call it outside the function, it won't work:

```py
print(my_string + "!!!!!!")
```

This is because of something called _scope_ which we'll go into more detail in next class. For now, know that the arguments you put in when you create a function are only usable by that function. 

### Functions with Return Values

So far we have used functions basically to call print statements to output something. However, your functions can also do other things (and usually do)! They can have _return values_, which are basically a satement at the end of a function that tells it what to simply the function down to when it is run. Here's an example modifying our previous function:

```py
def excited_string(my_string):
    return my_string + "!!!!!!!"
excited_string("Hello")
print(excited_string("Hello"))
new_string = excited_string("My new string")
print(new_string)
```

You can also write functions to take multiple inputs and do something to both of them.

```py
def excited_string_adv(my_string, num):
    new_string = my_string + "!" * num
    return(new_string)
```

Stop here and go to Exercise 1. 

### Some More Mathematical Functions

We've been using strings so far so you can see how functions work with and without arguments and return values, but functions can really do anything you define them to do. Here's a few very quick examples. 

You can do mathematics:

```py
def times_two(num):
    return num*2

def adder(num1, num2):
    return num1 + num2
```

You can have conditionals, with multiple return statements:

```py
def is_equal(num1, num2):
    if num1 == num2:
        return "These numbers are equal."
    else:
        return "These are different numbers."
```

You can have loops inside functions:

```py
def multiadd(start, stop):
    my_sum = 0
    for i in range(start, stop+1):
        my_sum += i
    return my_sum
```

Again, anything you could do outside a function, you can do inside a function. The key difference is when you define a function, you give it some arguments that the inside of the function can use. Which means that if you give it different arguments, you get to re-use the same code for a new purpose.

Let's turn one of our past in-class exercises for an example of something we could turn into a function. 

```py
counter = 0
num = input("Enter a number:" )
while num > 1:
    num = num//2 
    counter += 1
    print("Number: ", num)
print("Counter: ", counter)
```

Let's turn this into a function that takes in a number and just returns the counter. Remember this is (approximately) the log base 2. 

```py
def approx_log(num):
    counter = 0
    while num > 1:
        num = num//2 
        counter += 1
    return counter

print(approx_log(16))
```

Q: How would you alter this to be able to divide by some other value? i.e. What if instead of dividing by 2, we wanted division by 3? 

Go to in-class exercise 2. 

## In-Class Exercises

### Exercise 1

Write a function `exponent()` that takes two numbers, called _n1_ and _n2_ as inputs, and returns _n1_ raised to the power of _n2_. 

Here's some sample code.

```py
ex1 = exponent(7, 3)
ex2 = exponent(4, 2)
ex3 = exponent(25, 0.5)
print(ex1) # this should print 343
print(ex2) # this should print 16
print(ex3) # this should print 5
```

**CAREFUL!** Exponents are large. I would recommend when testing this out that you don't make _n2_ much larger than, say, 5. It won't hurt your computer or anything, but just to keep it reasonable. 

### Exercise 2

#### Part A

Turn your Collatz Conjecture code from Part 1B of last lab into a function. Specifically, write a function called `collatz()` that:

1. Takes in a number, `num`, as its argument.
2. Prints out the chain from the number to 1.

#### Part B

Turn your Collatz Conjecture code from Part 2B of last lab into a function. Specifically, write function called `longest_collatz()` that:

1. Takes in two numbers, `start` and `stop` **from the user**.
2. Returns (NOT prints) the number that the longest chain in that range started from. 

