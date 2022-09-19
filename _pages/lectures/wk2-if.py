my_number = 7
my_string = "CMSC 140"
my_bool = True

# and
print(True and True)
print(True and False)
print(False and False)

#or
print("T or T", True or True)
print("T or F", True or False)
print("F or T", False or True)
print("F or F", False or False)

# not
print("not T", not True)
print("not F", not False)

print(True and not (True or False))

## Comparison Operators

# equals / not equals
print("7 == 7", 7 == 7)
print("7 != 7", 7 != 7)
print("hello" == "hello") # True
print(True == False)
print(7 == "7")
print(1 + 2 == 3 - 0)
print("hi" + "hi" == "hi hi")

print("Greater Than/Equals to")
# greater than/ geq
print(7 > 5)
print(4 + 1 > 5)
print(4 + 1 >= 5)
print("a" < "b")
print("cow" < "cat")
print(True > True)
print(True >= True)

# less than /leq

print(7 < 5)
print(3 <= 2 + 2)


#print(my_number, my_string, my_bool)

#
print("in-class Exercises")
print(4 < 5)
print(True and False != True or True)
print((1 and 2) >= True == False)
print("cat" and "dog" >= ("dog" == "cat")) 
print(5 >= 3 and 2 == 4) 

# If Statements!

# if this statement is true:
#     do something

if True:
    print("Hello")

if False:
    print("Secret message that will never run")

i = 0 
if i == 0:
    print("i is 0")

i = 7
if i < 10:
    i = 10
    print(i)
    y = 25
    print(y)
    if 7 == 7:
        print("7 is 7")
    print(2 + 2)

print("i =", i)
print("i = " + str(i))

example = 20
if example < 10:
    print("Small number")
elif example == 10:
    print("It's 10!")
else:
    print("Big number.")

class_code = 100
if class_code == 140:
    print("This is Python")
elif class_code == 150:
    print("This is Java")
elif class_code == 270:
    print("This is Data Structures")
elif class_code >= 200 and class_code < 400:
    print("This is an upper level class")
elif class_code >= 400:
    print("This is an advanced class.")
#elif example == 20:
#    print("Example is 20 but I don't know the class code")
#else:
#    print("I don't know this class.")

case_key = 140

# this only works in python 3.10 and higher

match case_key:
    case 140:
        print("Python is cool")
    case 270:
        print("I love data structures")
    case 205 | 255: # if (case_key == 205) or (case_key == 225)
        print("This is a stats class")
