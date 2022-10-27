# Example of how to read and write a file in pandas
import pandas as pd
from pathlib import Path

datapath = Path("data") / "baseball.txt"
df = pd.read_csv(datapath, sep=",")
# subsetting like a list of lists
print(df["W"][5])
# using loc
print(df.loc[5, "W"])
# using iloc
print(df.iloc[5, 1])

# Creating new columns 
df["newcol"] = 0
df["anothercol"] = list(range(len(df)))

# Creating new columns from old columns
def ratio(row):
    w = row["W"]
    l = row["L"]
    return int(w)/int(l)
df["ratio"] = df.apply(lambda row: ratio(row), axis = 1)


# One way to find data in column based on another
idx_max = df["ratio"].idxmax()
print(df.loc[idx_max, "Team"])

# writing in python
outfile = Path("data") / "baseball_edited.csv"
df.to_csv(outfile, index_label="idx")
