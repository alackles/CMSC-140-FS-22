# while Loops

classcode = "CMSC 140"
if classcode == "CMSC 140":
    print("Welcome to class!")

# this is basically an if statement
while classcode == "CMSC 140":
    print("Welcome to class!")
    classcode = "CMSC 150" # change the code so the loop ends

print("The while loop is over.")
print(classcode)

times_through = 0
if times_through < 5:
    times_through = times_through + 1
    print("This has executed " + str(times_through) + " times.")
print("times_through:", times_through)

print("While Loop: ")

times_through = 0
while times_through < 5:
    times_through = times_through + 1
    print("This has executed " + str(times_through) + " times.")
print("times_through:", times_through)

print("New while loop: ")

num = 120348
while num > 1:
    num = num//2 
    print("Number: ", num)

# for loops

print("For Loop: ")
for times_through_for in range(5):
    print("This has executed " + str(times_through_for) + " times.")
print("times_through_for", times_through_for)

for i in range(10):
    print("For: " + str(i) + " squared is "  + str(i**2))

i = 0 
while i < 10:
    print("While: " + str(i) + " squared is "  + str(i**2))
    i += 1
