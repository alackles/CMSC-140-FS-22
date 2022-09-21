---
title: Homework 1
permalink: /hwk/hwk2/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---
# Homework 2: If/Else and Loops

**Due:** Thursday 9/29 @ 9:50 AM

**Learning Objectives**

- **L1**: Basics
- **L4**: Style

The purpose of this homework is to give you practice with if/else statements and with writing loops. Some of it might feel repetitive from things we do in class or in lab. That's because it is! It's meant to have a certain amount of repetition so that you become familiar with the structure of an if statement and a loop through repeated practice.

## Submission Guidelines

You will turn this homework to Canvas under **Homework 2**. 

You should submit your homework as separate files, one for each question. 

The first 4 files should `.py` files. The last file should be a `.pdf` file with a short response. 

Each should be named as `{familyname}_q{number}.{ext}`. For exapmle, my submissions would be:

`ackles_q1.py`  
`ackles_q2.py`  
`ackles_q3.py`  
`ackles_q4.py`  
`ackles_q5.pdf`  

(You can format your family name any way you want, just do not include spaces.)

Please remember to follow the [Collaboration Policy](https://alackles.github.io/CMSC-140-FS-22/syllabus/#collaboration-and-plagiarism) for all homework assignments.

## Homework Questions

### Q1: Adding Up

Write a `while` loop that calculates the sum of every number from 1 to 1000. Write a `for` loop that does the same. You can turn these in in the same file.

### Q2: Counting Down

Write a program that asks the user to input a number to start with. Then ask them to input a second number to count down by. Output the countdown, and don't output any numbers below 0. See below for example output:

```
Please enter a number to start from:
18
Please enter how much to count down by:
3
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
Please enter a number to start from:
18
Please enter how much to count down by: 
4
Countdown:
18
14
10
6
2
```

### Q3: Your Age

Write a program that asks the user what year they were born. Then, ask them if they have already had their birthday this year. Use this information to calculate their age.

The answer to the question "have you already had a birthday this year?" should accept all of the following inputs as possibilities:

- "Yes"
- "Y"
- "yes"
- "y"
- "No"
- "N"
- "no"
- "n"

When run, the output should look something like this.

```
Hello. What year were you born?:
1996
Have you already had a birthday this year?:
yes
You are 26 years old. 
```

### Q4: A Better Random Number Guesser

Last week you wrote a pretty poor random number guesser. In fact, it didn't really let the user guess anything at all.

Now, you have all the tools needed to change that!

Update your random number guesser from last week to do the following:

1. The number you choose should be between 1 and 100.
2. If the number the user guesses is higher than the chosen number, say "Too high."
3. If the number the user guesses is lower than the chosen number, say "Too low."
4. If the user does guess the number, it should say congrats, and end the program.
5. If the user doesn't guess the number, it should prompt them to guess again. 

For **mastery credit**, your number guesser should also choose the random number itself, and that number should be different every time the program is run. (Look into the python module `random`, which we used in class for Lab 2.) Remember to put some kind of limit on the number generated. 

For proficiency credit, it doesn't have to choose itself; you can choose. 

Here is some example output: 

```
Welcome to the random number guesser. 
Please input a number between 1 and 100:
50
50 is too high. Try again:
2
2 is too low. Try again:
38
38 is too low. Try again:
44
44 is too high. Try again:
43
Yes! 43 is the correct number.
```

### Q5: Loop Choices

Which kind of loop did you use for Question 2? Why did you choose this kind of loop? Is it possible to use the other kind of loop for this question? 

If not, explain why not. 

If yes, describe how you would do so.

Nothing formal (no code or proof) is required here, just an explanation of your thoughts as if you were answering a question in class. 


## Assessment

To demonstrate **Proficiency**, your code needs to produce the outputs specified above. Your written response needs provide some reflection on your choices.

To demonstrate **Mastery**, your code needs to produce the outputs specified above, and also have: 

- Descriptive variable names
- Useful (but not excessive) comments
- Good spacing

Your written response needs to correctly identify whether it is possible to choose an alternative kind of loop or not and provide a clear explanation as to why.