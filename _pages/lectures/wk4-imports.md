---
title: Week 4 Day 1 - Import 
permalink: /lectures/wk4-imports/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

View the code for the class on Github [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk4-imports.py).
# Imports

I've been promising we're going to learn about imports for a while now, so we're finally going to do the crash-course. 

## Basics of Import

Python has a number of built-in functions that we've talked about before. For example, you can find the length of a string with `len()`. But sometimes there is functionality that you want, but that isn't default in Python. 

One option we've seen so far is to write our own function to do what we want. But sometimes, other people have written those functions for us already, especially simple kinds of functions. 

For a number of common tasks, we don't have to reinvent the wheel; we can import a _module_ that contains multiple functions and use those functions directly. 

## Example 1: Math

To import a module in Python, you just have to ask Python to do so at the top of your code (and you need to know the module's name)

```py
import math 
```

Now you can use anything in the `math` module. You can find documentation about what's in the `math` module and how it works [here](https://docs.python.org/3/library/math.html).

To tell python the function you're using comes from the math module, and not from default python or your own functions, you have to preface every function with `math.` For example:

```py
a = math.ceil(2.4) # 3
b = math.factorial(5) # 120
pi = math.pi
```

## Example 2: Random

Another module that has been alluded to several times is random. Like with math, we can do:

```py
import random
```

You can use `random` to generate random numbers:

```py
num1 = random.randint(0,10)
num2 = random.randint(0,10)
num3 = random.randint(0,10)
```

Notice that `random` is a bit annoying to type out every time. We can actually change the name of the module when we import it:

```py
import random as rand
```

Now it works the same way as before:

```py
num1 = rand.randint(0,10)
num2 = rand.randint(0,10)
num3 = rand.randint(0,10)
```

Technical note: `random` requires a random seed, because it isn't truly random. If you don't set a seed, it uses your system's time as the seed, so it changes constantly. If you do set a seed, it will use that same seed every time. If you're curious what this means, try running this:

```py
import random

random.randseed(2)
num1 = random.randint(0,10)
num2 = random.randint(0,10)
```

Run this program multiple times, and `num1` and `num2` will always be the same. Changing the seed will change this behavior. 

## More Imports?

There are lots and lots of Python modules you could import; this just touches on a few of them so you know what it means. Later in the course we might use more modules; now you have a few to start with, and if you ever encounter a problem and find someone suggesting to use a module, you'll know how to use it. 