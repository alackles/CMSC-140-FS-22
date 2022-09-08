---
title: Install Python (Windows)
permalink: /guides/install-windows/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

# Installing Python (Windows)

This short guide will walk you through installing Python on your Windows computer. This guide assumes you are _not_ using WSL. If you don't know what that means, you probably aren't using it. 

## Check your operating system

In Windows, you can do this by going to :

**Start ▶ Settings ▶ System ▶ About**

Under _System Type_, it will say 64-bit or 32-bit. 

If you are having trouble finding this, you can also consult [this page](https://helpcenter.trendmicro.com/en-us/article/tmka-14342).

It's likely you are running 64-bit at this point, but it's possible you have a 32-bit operating system still. This might cause problems for you later on as most software is updating to support 64-bit only; **let me know if you have a 32-bit system.**

## Install Python

You can download Python at https://www.python.org/downloads/.

In **most cases**, you should just click the big yellow button in the middle of the page and follow your normal install steps, making sure to select a 64-bit operating system. 

The exceptions are if you have **a 32-bit system** or **an operating system before Windows 8 (Windows 7 or Windows Vista)**.

If you have a 32-bit system, download the latest release and install as 32-bit. 

If you have Windows 7 or Windows Vista, download **Python 3.8.9** at this link (scroll to the bottom): [Download](https://www.python.org/downloads/release/python-389/).

## Install PIP

PIP is a package manager for Python. It allows you to install some of the Python features that are helpful for various projects but don't come pre-packaged with your Python install. 

First, open your **Command Prompt** by clicking the start menu and typing `cmd`.

This should bring up basically a black window with some text. We'll work more with this in our first lab; for now, just know this is what your computer really looks like, without all the graphics interface!

To prove it, try typing `dir`. This should show you all your current directories (folders) on your computer. 

### Check if PIP is installed

First check if you already have pip installed for some reason by typing

```
pip --version
```

If something like `pip 22.2.2 from /usr/lib/python3.10/site-packages/pip (python 3.10)` comes up, that means you have pip installed.

If nothing comes up, you don't have pip.

### Install PIP if not installed

The easiest way to install PIP is to basically download a python program that installs PIP. 

You can do this most easily by copying and pasting the following into your command prompt:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

The basics of what this does:

- `curl` tells the computer to grab a file hosted online
- `https://bootstrap.pypa.io/get-pip.py` is the web address of that file
- `-o` tells the computer to copy that file to a new file on your computer
- `get-pip.py` is the name of that file on your computer; it will download it to whever you currently are in your directory when you open the command prompt

Try typing `dir` after this to see your directory again; you should now see a file called `get-pip.py`. 

Now, you will just have to run `get-pip.py` as a python script:

```
python get-pip.py
```

After this runs, try running `pip --version` again. This time, it should pop up. 

## Optional: Install VSCode

For this class, I'll be conducting my examples in VSCode, a free editing software for programming. it comes with lots of extnesions and features that make it really nice for programming, and if you use it, I'll probably be more familiar and able to help you better.

However, I don't want to force any particular software on you, as I think that can hinder your exploration of programming. So if you have a different software you _already use_ and prefer, you can keep that. 

### VSCode Website

You can download VSCode for Windows [here](https://code.visualstudio.com/download). Just click the big blue button and install as normal.

### VSCode Extensions

When you first start VSCode, it will walk you through a lot of its features; feel free to explore these all you want. 

Importantly, pay attention to the **Extensions** tab on the left; it looks like four squares, with the top right disconnected. These extensions install additional features that will make it easier to work with any programming language you're interested in. 

I suggest searching and installing the following:

- **Python** by Microsoft -- for better Python suggestions
- **GitLens** by GitKraken -- for integration with GitHub 
- **Rainbow CSV** by mechatroner -- for easier-to-read files, when we get there

You can also feel free to install other extensions that you just think might be fun. For example, I've installed **Dracula Official** as a color theme.

