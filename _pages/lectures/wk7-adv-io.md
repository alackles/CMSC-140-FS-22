---
title: Week 7 Day 1 - Advanced File I/O
permalink: /lectures/wk7-adv-io/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

# Lecture/Live Code

Here is the code for this week:

[Advanced File I/O](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk7-adv-io.py)

[More Pandas](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/wk7-pandas.py)

Recall last week we learned the basics of file input and output with base Python. Today we're extending on that by introducing Pandas, a poewrful python module designed for manipulation of data tables. 

## Review

Last class we discovered how to read in data and plot it. Here's a quick recap. 


```
temp hats
72 2
42 18
60 19
77 5
88 4
21 20
38 22
```

```py
import matplotlib.pyplot as plt
temps = []
hats = []
with open("hats.txt") as f:
    next(f) # this allows us to skip the first line, which is header text
    for line in f.readlines():
        t, h = line.split(" ")
        temps.append(t)
        hats.append(h)
plt.plot(temps, hats)
plt.show()
```

We can do more things with this data now that we have it as we read through the file, like perhaps we want to find the maximum number of hats and check the temperature on that day. 

```py
def get_temp(filename):
    max_hats = 0
    max_temp = 0
    with open(filename) as f:
        next(f) # this allows us to skip the first line, which is header text
        for line in f.readlines():
            t, h = line.split(" ")
            if h > max_hats:
                max_hats = h
                max_temp = t
    return max_temp
```

Let's try a similar thing with some new data. 

Go to In-Class Exercise 1

## Pandas

Reading in tabular data like this is a very common use of Python, so there are a lot of prewritten modules that make it easier to do things like this. 

One of them is pandas, which handles files in CSV format. CSV file format is basically how things like excel spreadsheets are stored. If you've used R, you'll be familiar with a lot of the syntax of Pandas.

Pandas has a lot of features, so we'll just look at a few of them. Here's a good supplementary guide to these notes if this all makes good sense to you, or if you have some experience with R and want to know how to do similar things in Python.

[Supplement.](https://medium.com/bhavaniravi/python-pandas-tutorial-92018da85a33)

### Installing Pandas

First we have to install Pandas with

```
pip3 install pandas
```

Check if it's installed by running a python script with the following:

```py
import pandas as pd
prof_info = {
    "Ackles" : {
        "classes": ["Python", "Algorithms"],
        "office": "Steitz 131",
        "firstname": "Acacia"
    },
    "Krebsbach" : {
        "classes": ["Java", "FYS"],
        "office": "Briggs 411"
    },
    "Gregg" : {
        "classes": ["Web Devel", "Algorithms"],
        "office": "Briggs 413"

    }
}
df = pd.DataFrame(data=prof_info)
print(df)
```

Now we have a table with all of this information, instead of a dictionary. 

### Reading to Pandas

We can read an entire file directly into a pandas dataframe with `read_csv`.

Take the example of the temps file from earlier.

```py
hattemps = pd.read_csv("hats.txt", sep = " ")
```

Note that it doesn't actually have to be a csv, just saved in csv format.

Note also that this automatically detects the header row!

### Working with Data

There are many, many things you can do with data in Pandas. Here are a few common ones. 

Indexing:

```py
templist = df["temps"]
temp = df["temps"][4]
```

Or `.loc` and `.iloc`

```py
t1 = df.loc[2, "temp"]
t2 = df.iloc[2, 0]
```

Changing names:

```py
df = df.rename(columns={"hats": "num_hats"})
```

or

```py
df.rename(columns={"num_hats": "hats"}, inplace=True)
```

Same for rows, but use _index_.


Creating columns from other columns:

```py
def isWarm(temp):
    return row['temp'] > 70

df['warm'] = df.apply(lambda row: isWarm(row), axis =1)
```

### Writing from Pandas

Finally, we can write out from pandas to a new file.

```py
df.write_csv("new_temps.csv")
```

# In-Class Exercises

## Exercise 1

Download (or copy & paste into a file) [this text file](https://github.com/alackles/CMSC-140-FS-22/blob/main/_pages/lectures/baseball.txt) containing the win-loss records of all the Major League Baseball teams for 2022 (sourced from [here](https://www.baseball-reference.com/leagues/majors/2022-standings.shtml)). 

Write a Python script to read in the information and output the name of the statistically best team; that is, the one with the highest ratio of Wins to Losses.

## Exercise 2

Do the same as above with pandas syntax.