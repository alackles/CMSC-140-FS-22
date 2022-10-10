---
title: Week 4 Day 2 - Dictionaries
permalink: /lectures/wk4-dicts/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

View the code for the class on Github [here](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk4-dicts.py).

# Dictionaries

We learned last class about lists, which are collections of values indexable by integers. This class we'll talk about dictionaries, which are also collections of values, but are indexable by basically anything you want. 

If you are coming from Java, these take the place of hashmaps. If you are coming from C++, they take the place of maps. 

## Lecture/Live Code

### Recap on Lists

We're going to do a short recap on lists, because lists are important but often confusing. 

Here's some information you might think about storing in a list: 

```py
profs = ["Ackles", "Krebsbach", "Gregg"]
```

Then you could iterate over that list to print some information:

```py
for name in profs:
    print(name + " is a CMSC professor.")
```

You could also add to the list:

```py
profs.append("Sage")
```

And you can remove items from a list: 

```py
profs.remove("Sage")
```

You might have other things you want to know about each of these professors, though, like what classes they're each teaching, or what their office is, or some other piece or pieces of information related to that person. This kind of mapping is where dictionaries become helpful. 

### Dictionaries

A dictionary is a collection of _values_ that are indexed by _keys_. You use them when you want to connect two values in an explicit way.

You create them in Python using curly braces, like this:

```py
profs = {"Ackles": "Steitz 131", "Krebsbach": "Briggs 411", "Gregg": "Briggs 413"}
```

Then you can access particular elements with the same indexing format you would a list. 

```py
print(profs["Ackles"])
```

You can print this dictionary as normal with `print(profs)`, but you can also access _just_ the values, or _just_ the keys:

```py
print(profs.keys())
print(profs.values())
```

You can even loop over these lists:

```py
for k in profs.keys():
    print(k)

for v in profs.values():
    print(v)

for i in profs.items():
    print(i)
```

Finally, you can use a multiple assignment trick to access both the keys and values at the same time:

```py
for k, v in profs.items():
    print(k + "'s office is in " + v)
```

Go to in-class exercise 1.

### Adding to Dictionaries

You can add to a dictionary by just assigning a new key-value pair. 

```py
profs["Sage"] = "Briggs 417"
print(profs)
```

This is also how you would change an item in a dictionary.

```py
profs["Ackles"] = "the moon"
print(profs)
```

#### Checking a Dictionary

Sometimes you want to check if a value is in a dictionary before doing something to it. You do this using the keyword `in`.

```py
print("Ackles" in profs)
print("Sattler" in profs)
```

Similarly you can do `not in`.

```py
print("Ackles" not in profs)
print("Sattler" not in profs)
```

PS: This works with lists and strings, too. 

#### Adding + Checking

Sometimes you want to add something to a dictionary only if it's not in there first, and maybe do something different if it is. One way is to use the if-else command. 

```py
if "Corry" in profs:
    print("Already added.")
else:
    profs["Corry"] = "Briggs 412"
```

If you don't need it to tell you anything if it's already in there, you could do:

```py
if "Corry" not in profs:
    profs["Corry"] = "Briggs 412"
```

Go to In-Class Exercise 2. 

### Lists as Values

It's possible to include more than just a single value as the 'value' part of a dictionary. Take the earlier example of wanting to know what classes every professor is teaching. This would require a list, like so:

```py
profs = {"Ackles": ["Intro Python", "Algorithms"], 
"Krebsbach": ["Intro Java", "First-Year Studies"], 
"Gregg": ["Web Development", "Algorithms"]}
```

Notice that here, the line breaks don't matter; that's because python knows it should be looking for that closed parentheses.

But now, we can print this as normal:

```py
for name, classes in profs.items():
    print("Name: ", name, "   Classes: ", classes)
```

We can even iterate through the lists, just as before. 

```py
for name, classes in profs.items():
    print("Name:", name)
    for classnum, classname in enumerate(classes):
        print("Class " + str(classnum) + ": " + classname)
    print("")
```

### Dictionaries as Values

Frequently, you want to hold a lot of nested pieces of information in a dictionary. Fortunately, dictionary values can themselves be dictionaries. 

Let's combine our two professor dictionaries from before. 

```py
profs = {
    "Ackles" : {
        "classes": ["Python", "Algorithms"], 
        "office": "Steitz 131"
    },
    "Gregg" : {
        "classes": ["Web Devel", "Algorithms"],
        "office": "Briggs 413"
    },
    "Krebsbach" : {
        "classes" : ["Java", "FYS"],
        "office": "Briggs 411"
    }
}
```

You can then access this with nested indices, like so:

```py
print(profs["Ackles"]["classes"])
```

And loop through:

```py
for prof, profdict in profs.items():
    print("Prof:", prof)
    for key, val in profdict.items():
        print(key, val)
```

This is something you'll have to do on the homework!

### Shortcuts for Common Features

To set a value only if it hasn't already been added to the dictionary:

```py
profs.setdefault('Corry', 'Briggs 419')
```

To get a value only if it is already in the dictionary:

```py
profs.get('Chakraborty', 'some other office')
profs.get('Ackles', 'some other office')
```

## In-Class Exercises

### Exercise 1

Turn the following into key-value pairs in a dictionary called `practice_dict`. 

```
Key: 5           Value: 20
Key: 2           Value: "Hello"
Key: "Hello"     Value: 5
```

Then, complete this for loop to print out the keys and values:

```py
for ##YOUR CODE HERE##:
    print("Key is:", key, "  Value is: ",value)
```

### Exercise 2

Put the following dictionary (you can copy-paste) and the following list into your code. 

```
fridge = {
    "eggs" : 12,
    "milk" : 1,
    "cheese" : 2,
    "bread" : 3,
    "pizza" : 0.5
}

shopping_needs = ["eggs", "fruit", "milk", "juice"]
```

Write a program that iterates through the list `shopping_needs` and for every item does the following:

1. If the item in the dictionary `fridge`, print how many are in there (its value), for example, "You already have ITEMNUMBER ITEMNAME."
2. If the item is not in the dictionary `fridge`, print something like "ITEMNAME is not in the fridge."