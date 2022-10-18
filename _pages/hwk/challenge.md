---
title: Challenge Questions
permalink: /hwk/challenge/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

These challenge questions are intended to go beyond what we talk about in class and introduce you to some complexities of Python syntax. 

You can turn in up to **two** of these questions to replace your Mastery score on their corresponding homework assignment. For example, if you got an IC, N, or P on Homework 3, you can complete Challenge Question 3 for that assignment instead of revising the assignment itself. 

If you wish to submit these for mastery credit, submit them to the associated homework assignment.

_There's no Challenge Question 1 because there's not much you can do with just variables to make this interesting._

# Challenge Question 2: If/Else & Loops

A popular feature in Python is _list comprehension_. You can read more about list comprehension in [this article](https://www.w3schools.com/python/python_lists_comprehension.asp) and at Python's [documentation](https://www.w3schools.com/python/python_lists_comprehension.asp).

Short is not always better--list comprehensions are helpful, but can often be difficult to read. However, it's nice to know how they work.

Important to know is that a list comprehension creates a generator object, which is not itself a list but acts like one in many contexts (what it actually is is outside the scope of this course, but come talk to me if you're curious). In particular, it can be converted to a string with `.join()` just like a list can.

**Question:** Write a one-line program, using list comprehensions, which prints out every even number between 1 and 100 unless that number is divisible by 3; in that case, print "threes!" instead. 

# Challenge Question 3: Functions

A common but tricky concept in computer programming is _recursion_. Recursion is when a function calls itself, usually with a modified input, so that the output of calls to the function with smaller inputs can be used as part of the solution for larger inputs. The recursion "bottoms out" with some base value. 

Here are some additional resources on recursion: [1](https://www.programiz.com/python-programming/recursion), [2](https://www.geeksforgeeks.org/recursion-in-python/).

As an example, here is a recursive function to calculate the sum of all numbers between 0 and some input n.

```py
def recursum(n):
    if n == 0:
        return 0
    else:
        return n + recursum(n-1)
```

We have some base case, the smallest possible input: if n = 0, then we return 0.

For all other inputs, we can represent the sum as follows:

```
sum(n) = sum(n-1) + n
```

So this becomes our recursive call. 

Another thing you could calculate recursively is the binomial coefficient, $$n \choose k\$$, read _n choose k_. This often comes up in statistics and combinatorics.

$${n \choose k} = \frac{n!}{(n-k)! k!}$$

Where ! is the [factorial](https://en.wikipedia.org/wiki/Factorial) operator.

**Note!** We must have $$k < n$$

$n \choose k$ can be written recursively as follows:

$${n \choose k} = {n -1 \choose k-1} + {n-1 \choose k}$$

With the following base cases:

$${n \choose n} = {n \choose 0} = 1$$

**Question:** Write a function which calculates $n \choose k$ recursively. 
# Challenge Question 4: Lists & Dictionaries

If you run the following code, you might find it does not do what you expect. 

```py
my_list = [2, 9, 20, 54]
new_list = my_list
new_list[0] = 11
print(my_list)
print(new_list)
```

It is probably surprising that changing something in`new_list` changes that same thing in `my_list`. 

This challenge question is a written response:

1. Does this happen with variables that store integers? With structures other than lists? **In particular, check if this happens for key-value assignment in dictionaries.** Do a little exploration, then come up with a theory for what is happening.
2. Read [this article](https://levelup.gitconnected.com/understanding-reference-and-copy-in-python-c681341a0cd8) and then, in your own words, explain why changing `new_list` changes `my_list` in the above code. Feel free to look up other concepts referenced in the article that you don't understand.
3. Propose how to change the above code so the original list is not altered.