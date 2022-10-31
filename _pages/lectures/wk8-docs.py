import itertools as it
import random
import copy

dna = ['A', 'C', 'G', 'T']

print(list(it.product(dna, repeat=3)))

dna_product = it.product(dna, repeat=3)
for i in dna_product:
    print("".join(i))

subjects = ["English", "Math", "Science", "Humanities"]
# in-place
#random.shuffle(subjects)
#print(subjects)

new_list = random.sample(subjects, k = len(subjects))
print(new_list)
print(subjects)

## Error Handling

## Assert Statements

x = list(range(20))
#print(x[-1])
#assert x[-1] == 20 , f"Expected 20, got {x[-1]}"
print(max(x))

a = 2
b = a
b = 7
print(a, b)

orig_list = [2, 9, 20, 54]
new_list = copy.deepcopy(orig_list)
new_list[0] = 11
print(new_list, orig_list)
assert orig_list[0] == 2, f"Expected 2, got {orig_list[0]}"
for x in orig_list:
    if x == 2:
        print(x)

# try except

x = input("Please enter a number: ")
try: 
    x = int(x)
    print(f"The square of your number is: {x**2}")
except ValueError: 
    print("Oops! You didn't enter a number.")
except:
    print("Something else went wrong.")

try:
    with open("data/baseball.txt") as f:
        print(list(line for line in f.readlines()))
    print(int("x"))
except FileNotFoundError:
    print("File not found.")
except:
    print("Something else went wrong.")
else:
    print("Nothing went wrong.")
finally:
    print("Done.")