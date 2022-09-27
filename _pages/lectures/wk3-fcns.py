 # functions!! 

print("Hello")
#num = input("Enter a number: ")
#print("Your number was: ", num)
name_length = len("Acacia")
print(name_length)

print(len("Acacia"))
print(4)
print(7 == 3)

my_sum = 0
for i in range(1, 21):
    my_sum += i 
print(my_sum)

my_sum = 0
for i in range(1, 101):
    my_sum += i 
print(my_sum) 

def our_first_function():
    print("This is a function")
    a = 7 + 2 
    print(a)

print("This is before the function.")
our_first_function()
our_first_function()
our_first_function()
our_first_function()
print("This is after the function.")

def excited_print(my_string):
    return my_string + "!!!!!!"
string1 = excited_print("Hello")
string2 = excited_print("This is a function")
print(string1)
print(string2)

def adder(num1, num2):
    my_sum = num1 + num2
    return my_sum
new_sum = adder(1, 4)
square_of_sum = new_sum**2
print(square_of_sum)


def number_add_2(num):
    return num+2
print(number_add_2(73))

def is_equal(num1, num2):
    if num1 == num2:
        return "This is equal"
    else:
        return "They are not equal"
is_equal(7, 8)
is_equal(1, 1)
print(is_equal(4, 2 + 2))
is_equal("hello", "hello")

def new_adder(start, stop):
    my_sum = 0
    for i in range(start, stop+1):
        my_sum += i
    return my_sum
    return my_sum + 2
    print("hello there")
print(new_adder(1000, 2500))
print(new_adder(3, 4))

def return_7(arg1, arg2, arg3):
    my_number = arg1 + arg2
    this_cool_string = "print out " + str(arg3) + "!!!!"
    y = arg2
    return my_number, this_cool_string
#function_result = return_7(2, 3, 4)
#print(function_result)


def approx_log(num, div):
    counter = 0 
    while num > 1:
        num = num//div 
        counter += 1
    return counter

ex1 = approx_log(25,2)
ex2 = approx_log(16,2)
print(ex1)
print(ex2)

ex3 = approx_log(25,3)
ex4 = approx_log(16,3)
print(ex3)
print(ex4)



num = 0
def incrementer():
    num += 1
    return num

print(num)
print(incrementer())