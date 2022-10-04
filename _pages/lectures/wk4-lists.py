import random

a = 4
b = 5
c = 2
d = 100
e = 29485020

my_list = [4, 5, 2, 100, 29248082]
print(my_list)

pet_names = ["Peanut", "Napoleon", "Llewyn", "Juniper", "Spike"]
mixed_list = [2, "string_ex", True, 2.4859]
print(pet_names)
print(mixed_list)

a = pet_names[0]
b = pet_names[3]
print(a, b)

c = pet_names[-1]
print(c)

cats = pet_names[:3]
other_animals = pet_names[3:]
print(cats)
print(other_animals)

a = "Hello"
print(a)
a = "Goodbye"
print(a)

pet_names[0] = "Baby"
print(pet_names)
pet_names[1] = pet_names[0]
print(pet_names)

list_a = [1, 2, 3]
list_b = ['x', 'y', 'z']
final_list = list_b + list_a
print(final_list)

numbers = []
print(numbers)
for i in range(5):
    numbers = numbers + [i]
    print(numbers)

for item in final_list:
    print("List")
    print(item)

nums = [1, 2, 100, 5]
for i in nums: 
    print("Square of" ,i, "is", i**2)

numbers = []
example_list = []
for i in range(20):
    #numbers = numbers + [random.randint(0, 100)]
    numbers.append(random.randint(0,100))
    example_list.append(i)
print(numbers)
print(example_list)

numbers.sort()
print(numbers)

list_size = [0] * 20
print(list_size)

print(pet_names)

for i, name in enumerate(pet_names):
    print(i, name)
