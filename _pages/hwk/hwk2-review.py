# Q3

curyear = 2022
birthyear = int(input("What year were you born?: "))

ans = input("Have you already had a bithday this year?: ")

if ans == "yes" or "y" or "Yes" or "Y":
    age = curyear - birthyear
elif ans == "no" or "n" or "No" or "N":
    age = curyear - birthyear  - 1

print("You are "+ str(age) + " years old.")