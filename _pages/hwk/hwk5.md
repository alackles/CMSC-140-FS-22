---
title: Homework 5
permalink: /hwk/hwk5/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

# Homework 5: String Operations & Regex


**Due:** Thursday 10/13 @ 9:50 AM

**Learning Objectives**

- **L1**: Basics
- **L4**: Style

The purpose of this homework is to get you used to string manipulation before we move into file input and output next week. It's also to reinforce ideas about functions, lists, and dictionaries.  

## Submission Guidelines

You will turn this homework to Canvas under **Homework 5**. 

You should submit your homework as separate files, one for each question. 

All files should be `.py` files. 

You can name the files any way you want as long as it's clear which files correspond to which questions. 

Please remember to follow the [Collaboration Policy](https://alackles.github.io/CMSC-140-FS-22/syllabus/#collaboration-and-plagiarism) for all homework assignments.

## Homework Questions

### Q1: AlTeRnAtInG CaSe

Write a function that takes in a single string as input and returns the string with alternating case. 

Example:

```py
string = "Hello class!!"
new_string = alt_case(string)
print(new_string) #HeLlO cLaSs!!
```

Notice that the alternation should pick up again after the whitespace. 

### Q2: Major Courses

Here is a partial list of courses for an interdisciplinary bio/physics/geography major here at Lawrence.

```py
major_courses = [
    "BIOL 130",
    "BIOL 150",
    "BIOL 280",
    "PHYS 141",
    "PHYS 151",
    "GEOL 110",
    "GEOS 210",
    "BIOL 650"
]
```

Write a program that creates a new list, `bio_courses`, containing only the numerical course codes for those courses which begin with "BIOL". The course codes should be integers. 

**This program should contain at least one function.** This function do anything related to the program; it can handle the entire problem, or just a piece of the problem. It's your choice where to put the function.

Your program should print the complete list of integers.

Example output:
```
[130, 150, 280, 650]
```

Note that these are integers, not strings.

### Q3: Regex Practice

Rewrite the Birthday Problem from previous homeworks, using a regex to check the input.

Here is the birthday problem:

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

**For Mastery credit**, you should also have some way of addressing input that is not one of the 8 options above. It is up to you how you choose to handle that input, but your program should not throw an error. 

## Assessment

To demonstrate **Proficiency**, your code needs to provide the outpus specified above. 

To demonstrate **Mastery**, your code needs to produce the outputs specified above, and also have: 

- Descriptive variable names
- Useful (but not excessive) comments
- Good spacing
- Well-organized logic
- Little redundancy

Note that good logic and less redundancy are now features of gaining mastery credit.

See also the additional mastery requirement for Q3.