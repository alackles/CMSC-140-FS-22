# Open a file
import matplotlib.pyplot as plt 

hello = open("hello.txt", 'r+')

# Read and/or Write

#file_contents = hello.read()
file_contents_list = hello.readlines()
#print(file_contents)
#print(file_contents_list)

hello.write("\nHere's some new content.")
# Can you open a dictionary?
#my_dict = open("example_dict.txt")
#my_dict_contents = my_dict.read()
#print(my_dict_contents)
# no :(

# Close the file

hello.close()

with open("goodbye.txt") as f:
    #info = [i.strip() for i in f.readlines()]
    info = f.readlines()

for i, val in enumerate(info):
    info[i] = val.strip()

temps = []
hats = []
with open("hats.txt") as f:
    next(f) # skip the first line
    for line in f.readlines():
        line = line.strip() # strip off the whitespace
        x, y = line.split(" ") # split the line on the space to get two different vals
        temps.append(int(x)) # append the first to our temps list
        hats.append(int(y)) # append the second to our hats list
print(temps)
print(hats)

plt.scatter(temps, hats)
plt.show()