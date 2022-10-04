---
title: Week 3 Day 2 - Scope
permalink: /lectures/wk3-scope/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

View the code for the class on Github [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk3-scope.py).
# Call Stack and Scope

For most of the previous classes we've been learning how to get Python to do certain things that we want it to do, but not necessarily how it operates. In many cases this is fine; we don't need to know every single thing the Python language is doing in order to write and execute our programs.

However, sometimes, it can be helpful to understand some more of the behind the scenes. So today is kind of a grab bag of topics in Python programming. 

We're going to start by talking about the _call stack_, or the order in which Python executes its statements. Then we're going to spend most of the day talking about _scope_, which is related to where Python is storing information about the programs we write.

There are no in-class exercises today. Instead, whatever time we have remaining, you will be free to work on the homework due tomorrow. You'll have a smoother time in lab if your homework is done before then, so I'm giving you an opportunity now to ask questions.

## The Call Stack

The call stack is a term for the order in which Python executes operations. As I alluded to last class, functions are run at the place where they are called, not at the place where they are written. 

```py
print("Start of Script.")

def outer_function():
    print("Outer Function Called.")

print("After function definition.")

outer_function()

print("After function called.")
```

However, it's also important to know that this is also true when functions are placed _inside other functions_. We've actually already seen that this is true with the `print()` function, but let's make it more explicit with our own defined functions.

```py
print("Start of Script.")

def outer_function():
    print("Outer Function Called.")
    inner_function()
    print("Outer Function Ends.")

def inner_function():
    print("Inner Function Called.")
    print("Inner Function Ends.")

print("End of Script.")
```

This order of execution is what's referred to as the call stack. It is handled behind the scenes and you usually don't have to worry too much about it, except to know when certain things will execute. 

Loops are another good example of a time when understanding the call stack, or the order of execution, is helpful to understand what's going on. 

Let's write a nested for loop.

```py
for i in range(5):
    for j in range(5):
        print("i =", i, "j =", j)
```

What do you think this will print for the first five lines?

Three options:

```
i = 0 j = 0.
i = 1 j = 1
i = 2 j = 2
i = 3 j = 3
i = 4 j = 4
```

```
i = 0 j = 0
i = 0 j = 1
i = 0 j = 2
i = 0 j = 3
i = 0 j = 4
```

```
i = 0 j = 0
i = 1 j = 0
i = 2 j = 0
i = 3 j = 0
i = 4 j = 0
```

Run it and try it out. 

The call stack for this nested for loop basically looks like this:

1. Enter the outer loop. Set i to 0.
2. Enter the inner loop. Set j to 0.
3. print the statement. 
4. Check the inner loop. Are we done? No -- set j to 1.
5. print the statement.
6. Check the inner loop. Are we done? No -- set j to 2.
7. print the statement.
8. Check the inner loop. Are we done? No -- set j to 3.
9. print the statement.
10. Check the inner loop. Are we done? No -- set j to 4.
11. print the statement.
12. Check the inner loop. Are we done? Yes.
13. Check the outer loop. Are we done? No -- set i to 1. 
14. **Enter the inner loop again.** Set j to 0.

and so on. The important thing here is that once the inner loop has executed all the way through, we return to that outer loop and we continue to execute it for its entire range. That means we may call the inner loop all over again, as many times as the outer loop requires. 

You might have been surprised that once we finish the inner loop, we still have to do it again; after all, hasn't `j` been incremented up to 5? To talk about that, we have to talk about scope. 

## Scope

Python has two scopes: local and global. 

_Local scope_ refers to anything happening within a particular function. _Global scope_ refers to anything happening outside a function, just in the basic file of the script itself. I'll draw a picture in class on the board and take a picture to paste in here after class. 

Variables in the local scope of a function are _local variables_. 

Variables in the global scope are _global variables_. 

Think of scope like a little quarantine for variables. You can create variables inside the box, and use them in there, but they can't leave. What happens in local scope stays in local scope. 

### Local Variables and Global Scope

Local variables **cannot** be used in global scope. You may have run into this before, but you will definitely run into it now that we will be spending more time with functions. 

```py
def add_num(num1, num2)
    new_sum = num1 + num2
    return new_sum

add_num(5, 8)
print(new_sum)
```

This will return an error, even though we've returned a value and everything. That's because `new_sum` is a local variable which is destroyed when the function ends. 

What could we do to actually print this sum? 

### Local Variables between Functions

A new local scope is created every time a function is called, so you can't use scopes between functions. 

```py
def file_namer():
    filename = "my_program.py"
    print(filename)

def file_reader():
    print(filename)

file_namer()
file_reader()
```


To fix the above program, we could do this and it will execute.

```py
def file_namer():
    filename = "my_program.py"
    print(filename)

def file_reader():
    filename = "my_thoughts.pdf"
    print(filename)

file_namer()
file_reader()
```
But these two filename variables are different. We can prove it here:

```py
def file_namer():
    filename = "my_program.py"
    file_reader()
    print(filename)

def file_reader():
    filename = "my_thoughts.pdf"
    print(filename)

file_namer()
file_reader()
```

Notice that the variable is only created and used within each function's own local scope. 

This is a good reason not to use the same variable name multiple times, even though you can; it can be confusing to read. We can edit our program to look a little less confusing. 

```py
def file_namer():
    filename_fn = "my_program.py"
    file_reader()
    print(filename_fn)

def file_reader():
    filename_fr = "my_thoughts.pdf"
    print(filename_fr)

file_namer()
file_reader()
```

Now you can see they're different. You should only have the same variable name in two different places if you really want to use the same variable. 

### Global Variables and Local Scope

You can read variables out of global scope into local scope, and you have in the past. Here's an example. 

```py
num = 0
def incrementer():
    new_num = num + 1
    return new_num

print(num)
print(incrementer())
print(num)
```

Since `num` here is a global variable, it can be accessed inside `incrementer()` and used. 

Here's something we can't do: 

```py
num = 0
def incrementer():
    num = num + 1
    return num

print(num)
print(incrementer())
print(num)
```

Because now we're not _using_ num, we are _declaring_ it as a variable. And we haven't set num to anything -- it's a local variable now, not global. So we can't add to something that doesn't exist yet. 

To avoid this kind of confusion, try to avoid referencing global variables inside local scopes. If you really want to do something to a variable you've declared in global scope, you could do it like this:

```py
num = 0
def incrementer(num):
    num = num + 1
    return num

print(num)
print(incrementer(num))
num = incrementer(num)
print(num)
```