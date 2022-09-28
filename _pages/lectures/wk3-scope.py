# Call stack

print("Start of Script")

print("Before function declaration")

def outer_function():
    print("Outer Function Called.")
    inner_function()
    print("Outer Function Ends.")

def inner_function():
    print("Inner function called.")
    print("Inner function ends.")

print("After function declaration")

outer_function()

# this is equiavlent to:
#    print("Outer Function Called.")
#    inner_function()
#    print("Outer Function Ends.")

print("After function call")

print("End of Script")

# Nested loops and the call stack

for i in range(5):
    for j in range(5):
        print("i = ", i, "j =", j)
        # if you wanted an inner while loop, you could add one
        #k = 0
        #while k < 2:
        #    k += 1
        #    print(k)
    # indentation matters
    # put a while loop here to run for the outer loop

# Scope

# Local variables cannot be used in global scope

def add_num(num1, num2):
    new_sum = num1 + num2
    #print(new_sum)
    return new_sum

add_num(5,8)
# a few different ways to print:

#x = add_num(5,7)
#print(x)

#print(add_num(5,8))

# this own't work though
#rint(new_sum)

def file_reader():
    filename_fr = "my_thoughts.pdf"
    print(filename_fr)

def file_namer():
    filename_fn = "my_program.py"
    file_reader()
    print(filename_fn)

file_reader()
file_namer()

# Reading variables from global scope

num = 0
def incrementer(number):
    number = number + 1
    return number

print(num)
print(incrementer(num))
num = incrementer(num)
print(num)