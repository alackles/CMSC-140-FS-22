import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

filepath = Path("data") / "hats.txt"

def plot_temps(filepath):
    temps = []
    hats = []
    with open(filepath) as f:
        next(f)
        for line in f.readlines():
            t, h = line.strip().split(" ")
            temps.append(int(t))
            hats.append(int(h))
    plt.scatter(temps, hats)
    plt.show()

def get_temp(filename):
    max_hats = 0
    max_temp = 0
    with open(filename) as f:
        next(f)
        for line in f.readlines():
            #t, h = [int(x) for x in line.strip().split(" ")]
            t, h = line.strip().split(" ")
            t = int(t)
            h = int(h)
            if h > max_hats:
                max_hats = h
                max_temp = t
    return max_temp, max_hats

def get_best_team(stats_file):
    best_team = ""
    best_record = 0
    with open(stats_file) as f:
        next(f)
        for line in f.readlines():
            name, win, loss = line.strip().split(",")
            record = int(win)/int(loss)
            if record > best_record:
                best_record = record
                best_team = name
    return best_team

def get_best_team_alt(stats_file):
    teamdict = {}
    with open(stats_file) as f:
        next(f)
        for line in f.readlines():
            name, win, loss = line.strip().split(",")
            teamdict[name] = int(win)/int(loss)
    max_val = 0
    max_key = ""
    for k, v in teamdict.items():
        if v > max_val:
            max_val = v
            max_key = k
    return max_key, teamdict

statspath = Path("data") / "baseball.txt"
#best_team = get_best_team_alt(statspath)
#print(best_team)

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

print(df["Ackles"]["classes"])
print(df.loc["classes", "Ackles"])
print(df.iloc[1,2])

teams_df = pd.read_csv(statspath, sep = ",")
# Write a function that operates on a row, and returns what you want the new row to look like
def win_loss(row):
    win = row['W']
    loss = row['L']
    return int(win)/int(loss)
# follow the format: df.apply(lambda row: function(row), axis = 1)
teams_df["ratio"] = teams_df.apply(lambda row: win_loss(row), axis = 1)
print(teams_df)



#max_temperature = get_temp(filepath)
#print(max_temperature)
#plot_temps(filepath)