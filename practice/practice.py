""" filename = "project2.pdf"

i = 0
while i < 5: 
    if filename == "project.pdf":
        # open the file
        print("The file is open.")
        print(filename)
    elif filename == "project2.pdf":
        print("The second file is open.")
        print(filename)
    else:
        print("Wrong filename.")
        print(filename)
    i += 1
    print(i)

 """

product = 1
number = 0
while number < 10:
    number += 1
    print(number)
    product *= number
    #[do something here]
print("product: ", product)

# for [iterator] in range([the range you want])

product = 1
for number in range(1,10+1):
    print("for num: ", number)
    product *= number
print("for product: ", product)

print("This string has \"quotation\" marks")