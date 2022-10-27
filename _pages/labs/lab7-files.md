---
title: Lab 7 - Files
permalink: /labs/lab7/
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

The purpose of this lab is to get some more practice with reading and writing files with Python. You can either use base python or Pandas for this lab. 

The secondary purpose of this lab is to **give you a refresher on using GitHub**. Remember that your final project will be turned in as a github repository; this lab will be turned in the same way. 

This is an individual lab so you can each get practice with github on your own machines; however, you're welcome to chat with each other if you're encountering problems. 

# Part 1: Retrieving the Data

**This part of the lab we will walk through together.**

## Forking

First, visit [this GitHub Repository](https://github.com/alackles/cmsc140-f22-lab7/). 

The first thing you'll need to do is _fork_ this repository, so that you have a copy that you have complete control over. To do this, click the Fork button in the top right corner. 

If you aren't in lab physically to walk through this with us, click [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo) for a guide on forking a repository. 

## Cloning

Next, you'll want to download this repository to your own computer so that you can work with it. This is called _cloning_. 

The command to do so is

```
git clone <REPOSITORY URL HERE> <FOLDER NAME HERE>
```

without any of the brackets. For example, if I wanted to clone my repository into a folder called `lab7`, I would type into my terminal:

```
git clone https://github.com/alackles/cmsc140-f22-lab7.git lab7
```

**Important:** Make certain that you are cloning YOUR fork, not my repository. Otherwise, you won't be able to push to it (save info back to github.)

Make sure you are at the place in your terminal that you want the file to be saved when you perform this cloning step. It will save the folder containing the repository to wherever you have saved However, you can always move the folder later. 

## Pushing

To check that everything is set up correctly, and to practice adding/committing/pushing, you should change something in the README.md file. You could add your name to this file, for example. 

Then if you type

```
git status
``` 

in your terminal, you should see that changes are made. Now you can go through the three-step process of syncing these changes to github.

### Add

First, add your changes to the "staging ground":

```
git add .
```

### Commit

Next, add a message that says what you've done.

```
git commit -m "Add name to README.md"
```

### Push

Finally, sync the changes back to GitHub.

```
git push
```

Now, if you go to your repository, you should see the changes to your README.md.

## Unzipping the Data

The last thing you'll have to do before actually starting on your lab is unzip the data in the zip file so you can work with it. You can do this on the terminal if you like, or you can do it however you normally extract zip files. If you have problems with this step, let me know. 

## gitignore

Now that your data is unzipped, you should create a file called `.gitignore` that has the name of your file in it. That is, the only content in the `.gitignore` file should be

```
city_temperature.csv
```

Add, commit, and push your `.gitignore` file to github. 

# Part 2: Explore your Data

This data holds average temperatures in various cities around the world every single day across multiple years.

You can glance at the data in VSCode; it's quite long! 

Each row is in the following format:

```
Region,Country,State,Month,Day,Year,AvgTemperature
```


# Part 3: Process your Data

Your task for this lab is to **find the hottest day in each region, and record that information in a new csv file**.

Part of this lab is deciding how to keep track of the hottest day in each region without knowing exactly what the regions are ahead of time, but to help you out, I can tell you there are x regions, so your CSV file should have x lines at the end.

See below for some hints to guide you through this process.

For this part, you can use **either** base Python or Pandas. **If you're someone taking this class for some data science experience, I strongly suggest using Pandas.**

## Option 1: Base Python

Here's the general outline of steps you should take:

1. First, figure out how to read in your file. Remember the `Path()` module and `with open() as` method.
2. Think about how you would solve a simpler problem first. How would you get the information for the maximum temperature across all the lines, without needing to split it up by region? Write this code first. 
3. Next, think about how to break this down into regions. You're basically going to do what you did before to find the maximum, but for each region. Therefore, when you read through the file line by line, how will you know if you've moved on to a new region? As a helpful hint, the regions are all in order; i.e., once you stop reading information for a region, it is over. 
4. Finally, you should write your new information out to a new `csv` file.

## Option 2: Pandas

Here's the general outline of steps you should take:

_Note: This method will require you to write less code and a lot of it will happen behind the scenes, so I'm giving you less instruction. Instead, you're getting practice reading documentation, which we'll talk about on Monday._

1. First, read in your file with `to_csv()`. 
2. Next, take a look at the Pandas `groupby()` method [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html?highlight=groupby#pandas.DataFrame.groupby). Pay particular attention towards some of the examples, especially the ones involving `.sum()`.
3. Next, take a look at the Pandas `max()` method [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.max.html). 
4. Figure out how to use these and any other necessary operations to create either a new dataframe or another data structure that you can write out into a new file. 

# Part 4: Re-Upload to GitHub

Upload your data to github with the add-commit-push steps, and submit the link to your repository to canvas. 
