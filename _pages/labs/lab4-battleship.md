---
title: Lab 4 - Mini Battleship
permalink: /labs/lab4/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

The purpose of this lab is to get more experience storing and retrieving data from lists and dictionaries. It's also to get you to start thinking about what it means to write a 'game' as a final project. 

**For this lab, you'll be working in groups at your tables.** Everyone should turn in a .py file; the top of the file should have two comments:

1. Who you worked with (everyone at your table)
2. What your contribution was (typing code, giving suggestions on particular parts of the problem, debugging, asking questions).

Otherwise, the contents should be identical; you'll only be working on a single file together this lab. 

**If you aren't physically present in lab, you can submit the lab individually. Just note that you were not in attendance in your comment.**

For the first part of the lab, one person should be typing and projecting their code onto the screens at your table; the other people should be giving suggestions. At each time when it says switch typing, pick someone else to type.  

# Battleship

Here, we're going to write a very small, one-sided version of the game Battleship. You'll have a 3x3 grid and only one ship. Your goal is to make function, `battleship()`, which when called starts a game the user can play that:

1. Lets one player select a location to place their battleship.
2. Lets the second player guess locations of the battleship until it is found.
3. At the end, output their number of guesses as a "score". 

You'll use dictionaries to do this. 

## Part I: Build a Battleship Board 

Select someone at your table to do the typing. 

First, you will need to build a blank battleship board, and have some way to print it out. Your battleship board will look something like this:

```
    A    B    C
1   .    .    .
2   .    .    .
3   .    .    .
```


Your instructions for Part I are:

1. Write a dictionary to represent the board where the keys are the columns (e.g. `"A"`, `"B"`, `"C"`) and the values are lists representing the rows.
2. Print out that board.

### Step 1: Write your dictionary

Some hints for this step: 

When you first write the board, every spot should be an '.'.

Each key (column) should have a list of just three elements to represent the rows. So the first element of the list at `board["A"]` should be whatever is at A1. The second element should be whatever is at A2. The last element should be whatever is at A3, and so on. 

### Step 2: Print the board

In the interest of time for this lab, I'm providing you with the print function. However, this function will only work if your board is of the form specified above!

```py
def print_board(board):
    print("     A    B    C")
    for i in range(len(board.values())):
        print(str(i+1) + "    " + board["A"][i] + "    " +  board["B"][i] + "    " + board["C"][i])
```

Call the `print_board()` function on your battleship board to see it print out. 

## Part II: Select your Battleship

For the next part of the lab, we will start building the function that allows a user to pick a battleship location and then to start guessing. This location shouldn't be displayed on the board, but instead stored elsewhere in the function. 

Write a function `battleship()` that takes a single argument, `board`, as its parameter. This argument should be the entire dictionary that holds the battleship board (just like the `print_board()` function.) For this part, the function should do the following:

1. When called, ask the user to input the location they want to put their battleship. 
2. Save that location in two new variables, one for the column and one for the row.
3. Print out the battleship board (still blank at this point) using the `print_board()` function. 


Your output when you run your python script should look something like this:

```
Welcome to Battleship!

Player 1, select a column for your battleship: A 
Player 1, select a row for your battleship: 2

Current Board:

    A    B    C
1   .    .    .
2   .    .    .
3   .    .    .
```

## Part III: Take a Guess

**Someone else should take over typing at this point**. 

Next, we need to add functionality that allows us to look for the ship. First, make sure you know how to take a single guess from the user. 

Add the following functionality to your `battleship()` function:

1. Take a single guess from the user about where the ship might be. Like before, take both the column and the row as separate inputs.
2. If the guess is correct, change the location to a "!" and print, "You won!"
3. If the guess is incorrect, change the location to a "x" and print, "Sorry, nothing there."
4. Print out the board either way. 

Here's two example outputs for this new script.


```
Welcome to Battleship!

Player 1, select a column for your battleship: A 
Player 1, select a row for your battleship: 2

Current Board:

    A    B    C
1   .    .    .
2   .    .    .
3   .    .    .

Player 2, select a column to check: A
Player 2, select a row to check: 3

Sorry, nothing there.

Current Board:

    A    B    C
1   .    .    .
2   .    .    .
3   x    .    .
```

```
Welcome to Battleship!

Player 1, select a column for your battleship: A 
Player 1, select a row for your battleship: 2

Current Board:

    A    B    C
1   .    .    .
2   .    .    .
3   .    .    .

Player 2, select a column to check: A
Player 2, select a row to check: 2

You won!

Current Board:

    A    B    C
1   .    .    .
2   .    !    .
3   .    .    .
```

## Part IV: Sink your Battleship

For the final part of this lab, you will need to do the following:

1. Let the user keep inputting guesses until they find the battleship, updating and printing the board every time.
2. Keep track of the number of guesses, and print this out as their score. 

Here's a sample output. 

```
Welcome to Battleship!

Player 1, select a column for your battleship: A 
Player 1, select a row for your battleship: 2

Current Board:

    A    B    C
1   .    .    .
2   .    .    .
3   .    .    .

Player 2, select a column to check: A
Player 2, select a row to check: 3

Sorry, nothing there.

Current Board:

    A    B    C
1   .    .    .
2   .    .    .
3   x    .    .

Player 2, select a column to check: C
Player 2, select a row to check: 1

Sorry, nothing there.

Current Board:

    A    B    C
1   .    .    x
2   .    .    .
3   x    .    .

Player 2, select a column to check: C
Player 2, select a row to check: 1

You won!

Current Board:

    A    B    C
1   .    .    x
2   .    !    .
3   x    .    .

Score: 3 Guesses
```

That's the end of the lab! Send the file you have been working on to each other at your table, and everyone should submit the lab to Canvas. **Note: You will need to change the extension to .txt if you are sending it via email, because Lawrence's email system doesn't like to send code. Then when you receive the file, you can change it back to .py**. The other option is to use GitHub.