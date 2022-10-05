---
title: Homework 3
permalink: /hwk/hwk3/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

# Homework 3: Functions

**Due:** Thursday 10/6 @ 9:50 AM

**Learning Objectives**

- **L1**: Basics
- **L4**: Style
- **L5**: Code Review

The purpose of this homework is to give you more practice writing functions and analyzing the kind of code we've looked at in class so far. Notice that you have an additional LO for this homework, Code Review, which is about your ability to read and understand code someone else has written. 

## Submission Guidelines

You will turn this homework to Canvas under **Homework 3**. 

You should submit your homework as separate files, one for each question. 

The first 2 files should `.py` files. The last 2 files should be a `.pdf` or `.txt` file with a short response. 

Each should be named as `{familyname}_q{number}.{ext}`. For exapmle, my submissions would be:

`ackles_q1.py`  
`ackles_q2.py`  
`ackles_q3.pdf`
`ackles_q4.pdf`  

(You can format your family name any way you want, just do not include spaces.)

Please remember to follow the [Collaboration Policy](https://alackles.github.io/CMSC-140-FS-22/syllabus/#collaboration-and-plagiarism) for all homework assignments.

## Homework Questions

### Q1: Collatz Conjecture (Redux)

Turn in Part B of Monday's in-class exercise for this homework question. Here is the problem as a refresher:

Write function called `longest_collatz()` that: 
- Takes in two numbers, start and stop from the user.
- Returns (NOT prints) the number that the longest chain in that range started from

Note that you are not printing the length of the longest chain, only the number it originated from.

You can use the wikipedia page on the Collatz Conjecture, which has [some longest chains in a particular range](https://en.wikipedia.org/wiki/Collatz_conjecture#Empirical_data), to check your work.


### Q2: A Functional Random Number Guesser

Last week you wrote a much better random number guesser than in previous weeks. Now, you can turn this into a function! (Are you sick of the random number guesser yet?)

Recall that your random number guesser from last week should have done the following:

1. The number you choose should be between 1 and 100.
2. If the number the user guesses is higher than the chosen number, say "Too high."
3. If the number the user guesses is lower than the chosen number, say "Too low."
4. If the user does guess the number, it should say congrats, and end the program.
5. If the user doesn't guess the number, it should prompt them to guess again.


You will now also add the following functionality:

1. The number guesser script should **generate its own random number**. (Hint: use the `random` module.) 
2. The number guesser should be a function, `random_number_guesser()`, which takes a single argument: the number of guesses a user has available.
3. The user should input the number of guesses they want to take.
4. The number guesser should tell the user how many guesses are left each time they guess a new number. 
5. If the user runs out of guesses, the number generator should stop and tell them sorry, but they lost, and print the correct number.

Here is some example output:

```
How many guesses?: 
7
Welcome to the random number guesser. 
Please input a number between 1 and 100:
50
50 is too high. Try again (6 guesses left):
2
2 is too low. Try again (5 guesses left):
38
38 is too low. Try again (4 guesses left):
44
44 is too high. Try again (3 guesses left):
43
Yes! 43 is the correct number.
```

Here is an alternative output:

```
How many guesses?: 
3
Welcome to the random number guesser. 
Please input a number between 1 and 100:
50
50 is too high. Try again (2 guesses left):
2
2 is too low. Try again (1 guesses left):
38
Sorry, you lost. The correct number was 43.
```


### Q3: Code Review

Consider the following code. 

```py
def silly_program():
    x = 0
    # Q2 MARKER
    while x < 2:
        for i in range(3):
            print(i)
            if i == 2:
                print(i, "is my favorite number")
        x += 1
x = 5 
# Q1 MARKER
print("This is my program.")
print(silly_program())
```

Answer the following questions in writing.

1. What is the value of `x` at `#Q1 MARKER`?
2. What is the value of `x` at `#Q2 MARKER`?
3. Are the `x` above Q1 MARKER and the `x` above Q2 MARKER the same variable? Why or why not?
4. Write out what this code will print. **Do not run the code before writing it out. You will only be evaluated on whether you have written something reasonable here, not its correctness.** 
5. Run the code to check your work. Note if your initial guess was different than on the code's output, and if so, why? What was different between the two, and do you understand why they were different? **You will be evaluated not on whether your initial guess was correct, but on your explanation of how running the code matched or didn't match to your initial guess.**

### Q4: Reflection

At this point, you've worked on your random number guesser three homeworks in a row. What was something you found confusing or challenging last time or on the first homework that makes more sense now? This can be conceptual (e.g., how to check if a number is the correct number) or procedural (e.g., remembering how to concatenate strings and ints).


## Assessment

To demonstrate **Proficiency**, your code for questions 1 and 2 need to provide the outpus specified above. Your written responses should be complete and address the questions asked.

To demonstrate **Mastery**, your code needs to produce the outputs specified above, and also have: 

- Descriptive variable names
- Useful (but not excessive) comments
- Good spacing

Your written responses should provide some insight into your thought process and learning thus far. Basically, it should be more detailed than just "I ran the code and it was different than mine, so I changed mine to match." or "I was having trouble with loops, but I think I get it now."  