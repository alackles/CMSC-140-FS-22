import re

# Step 1: Create your Regex
yes_regex = re.compile(r"(y|Y)")
no_regex = re.compile(r"(n|N)")

# Step 2: Compare your regex to a string
if re.match(yes_regex, "yellow"):
    print("match")
else:
    print("no match")