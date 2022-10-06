# Q3

curyear = 2022
birthyear = int(input("What year were you born?: "))

ans = input("Have you already had a bithday this year?: ")

if ans in ["yes","y", "Yes", "Y"]:
    age = curyear - birthyear
elif ans == "no" or ans=="n" or ans=="No" or ans=="N":
    age = curyear - birthyear  - 1

print("You are "+ str(age) + " years old.")