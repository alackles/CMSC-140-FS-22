---
title: Week 6 Day 1 - Pathing
permalink: /lectures/wk6-pathing/
toc: true
toc_label: "table of contents"
toc_icon: "cog"
---

Starting next class we'll be loading files into Python to work with their contents programmatically. Before we do that, though, we need to understand how the computer knows where files are stored, and how Python is able to use that information.

# Lecture/Live Code

## File Locations

Every file on your computer has a location. When we give files names, we are really adding that name onto a long string of characters that has your file's actual location inside the computer. 

To see what I mean, open up whatever file finder you usually use. Right-click or two-finger click on one of the folders or files, select _Properties_, and look for a line like _Location_. 

This is where your file is stored in your computer; the whole path from the root of your computer outwards. 

This is why your computer says you can't have two files with the same name in the same location, but it's okay to have files with the same name in different locations--because they don't really have the same name. 

## Python Pathing

Windows and Mac have different ways of writing file paths. Windows uses a backslash `\` while Mac (and Linux) uses a forward slash `/`. 

Python has ways to handle these discrepancies so that your code will work on any computer. We use the `Path` module. 

```py
from pathlib import Path
```

Notice that we're using a `from ... import` construction here. This is because we're only using a single function from `pathlib`, called `Path`, so we want to be able to call it without needing to specify the import slug beforehand. 

If this is confusing to you, you can do 

```py
import pathlib
```

And any time you need to use `Path()`, you can use `pathlib.Path()` instead.

The Path function takes a string representing a path in your computer and processes it for whatever operating system your code is running on. 

Here's an example. 

```py
home_dir = "/home/acacia"
home_path = Path(home_dir)
```

You can add to this homedir path with a forward slash:

```py
new_path = home_path / Documents
```

But at least one of the objects here must be a Path object. 

You can chain them, but at least one of the first two objects has to be a Path object. 

This makes it safe to run your code on any computer. A common thing to do is to make the base path to the project a stirng that the user can change at will, and then have folders that you provide stuck on the end so if they download your code, it will run with only one change. 

Example:

```py
from pathlib import Path
path_to_proj = "home/acacia/Documents/teaching/AY-22-23/fall/CMSC140/"
base_path = Path(path_to_proj)
pages_path = base_path / "_pages"
syllabus = base_path / "syllabus.md"
hwk_path = base_path / "_pages" / "hwk"
```

## Current Working Directory

If you want to quickly know where your code thinks it's being run from, you can do this:

```py
print(Path.cwd())
```

Which will give you the full filepath of where your script is currently running from. 

## Relative Pathing

Absolute paths are the ones we've been working with so far: from the root of your computer to where you are now. 

Relative pathing works a little differently; it looks for the location _where your file is being run from_ and goes from there. 

This means when we start working with files next week, if you're in the habit of clicking 'run' on your Python script, you'll need to make sure your relative paths are relative to where that is _run from_, not where your file is _saved_. 

