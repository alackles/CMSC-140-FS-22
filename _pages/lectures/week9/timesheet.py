import pandas as pd
from code.diffs import listdiff

timesheets = pd.read_csv("timesheet.csv", header=None)
original_time = list(timesheets[0])
changed_time = list(timesheets[1])

print(listdiff(original_time, changed_time))