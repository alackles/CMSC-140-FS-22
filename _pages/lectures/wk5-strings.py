# Escape characters

#ex_string = 'This won't work

double_quote = "This 'string' is okay"
single_quote = 'This "string" is okay'
print(double_quote, single_quote)

esc_double = "This is \"fine\" now."
esc_single = 'This string\\\'s formatting is okay.'
print(esc_double)
print(esc_single)

rawstring = r'This prints \' exactly " what I type.'
print(rawstring)

print("hello")
print("this is on a new line")

trip_quote = """This is a string
across multiple lines.
"""

newline = "This is a string\nwith a newline"
print(trip_quote)
print(newline)

name = "Acacia Lee Ackles"
print(name[0])
print(name[0:6])
print(name)

firstname = name[0:6]
print(firstname)

#name[0] = "K" <- doesn't work
#name.append("hello") <- doesn't work

print(firstname in name)
print("Hello" in "Hello")
print("j" in "fox")
print("j" not in "fox")

splitname = name.split()
print(splitname[0])
# for key,val in dict.items()

first, middle, last = name.split()
print(first)
print(middle)
print(last)

a, b = [0, 1]
print(a)
print(b)

print(name)
print(name.split('a'))

my_list = ["hello", "python", "class"]
nospace = "".join(my_list)
space = " ".join(my_list)
wee = "wheeee".join(my_list)
print(nospace)
print(space)
print(wee)

space_string = "This is a string with   a lot of    spaces!"
splitstring = space_string.split('a')
print(splitstring)
#print(splitstring[4])

a, b, c = ["hello", 2, True]
print(a)
print(b)
print(c)

print("-".join(["a", "b", "c"]))

print("-".join("These are spaces".split()))

# Strings in Strings

fruit = "apples"
num = 7

print("I have " + str(num + 1) + " " + fruit + "." )

# string interpolation

print("I have %s %s." % (num + 1, fruit))

# f-strings

print(f'I have {num + 1} {fruit}.')
print('I have {num + 1} {fruit}.')

## Formatting

newname = name.upper()
name = name.upper()
print(name)
print(newname)
newname2 = name.lower()
print(newname2)

print(newname.isupper())
print(name.isupper())


#age = int(input("How old are you?: "))
#birthday = input("Did you have a birthday this year?: ")
#birthyear = 2022 - age
#print("Input:", birthday)
#print("Input lower:", birthday.lower())
#if birthday.lower() == "yes" or birthday.lower() == "y":
#    print(f"You were born in {birthyear}.")
#else:
#    print(f"You were born in {birthyear-1}.")

space_string = "    Hello!    "
left = space_string.lstrip()
right = space_string.rstrip()
both = space_string.strip()
print(left)
print(right)
print(both)
print(left == both)

cool_string = "oooooo Hello ooooooooo"
print(cool_string.strip('ol '))

# Checking alphanumeric

print("abc".isalpha())
print("abc123".isalpha())
print("abc123".isalnum())
print("abc!!123".isalnum())

# Other things (int, lists)
print(isinstance(7, int))
print(isinstance("hello", int))
print(isinstance(name, str))
my_list = [7, 8, "list", [1, 2]]
print(isinstance(my_list, list))

if isinstance(my_list, list):
    print(my_list)

