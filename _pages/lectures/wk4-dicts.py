from cProfile import Profile


profs = ["Ackles", "Krebsbach", "Gregg"]

evens = list(range(0,20,2))

for i in range(len(evens)):
    print(str(i) + ": " + str(evens[i]))

for i, prof in enumerate(profs):
    print(str(i) + " " + prof + " is a CMSC professor.")

for i in range(len(profs)):
    print(str(i) + " " +  profs[i] + " is a CMSC professor.")

profs.append("Sage")
print(profs)

profs.remove("Sage")
print(profs)

## Dicts

prof_offices = { 
    "Ackles" : "Steitz 131", 
    "Krebsbach" : "Briggs 411", 
    "Gregg" : "Briggs 413"
    }
print(prof_offices)
print(prof_offices["Ackles"])
print(prof_offices.keys())
print(prof_offices.values())

for name in prof_offices.keys():
    print(name)

for office in prof_offices.values():
    print(office)

for name, office in prof_offices.items():
    print(name + " is in " + office)

prof_offices["Sage"] = "Briggs 417"
print(prof_offices)

#prof_offices["Ackles"] = "the moon"
#print(prof_offices)

print("Ackles" in prof_offices.keys()) # true
print("Ackles" in prof_offices) # true
print("Steitz 131" in prof_offices) # false
print("Steitz 131" in prof_offices.values()) # true
print("Sattler" not in prof_offices)

if "Corry" in prof_offices:
    print("Already added.")
else:
    prof_offices["Corry"] = "needs an office"

if "Corry" not in prof_offices:
    prof_offices["Corry"] = "needs an office"

print(prof_offices)

prof_classes = {
    "Ackles" : ["Intro Python", "Algorithms"],
    "Krebsbach" : ["Intro Java", "First Year Studies"],
    "Gregg" : ["Web Development", "Algorithms"]
}

for name, classes in prof_classes.items():
    print("Name: ", name, "   Classes: ", classes)

for name, classes in prof_classes.items():
    print("Name: ", name)
    for classname in classes:
        print(classname)

prof_info = {
    "Ackles" : {
        "classes": ["Python", "Algorithms"],
        "office": "Steitz 131",
        "firstname": "Acacia"
    },
    "Krebsbach" : {
        "classes": ["Java", "FYS"],
        "office": "Briggs 411"
    },
    "Gregg" : {
        "classes": ["Web Devel", "Algorithms"],
        "office": "Briggs 413"

    }
}

print(prof_info["Ackles"]["office"])

fridge = {
    "eggs" : 12,
    "milk" : 1,
    "cheese" : 2,
    "bread" : 3,
    "pizza" : 0.5
}
shopping_needs = ["eggs", "fruit", "milk", "juice"]

for item in shopping_needs:
    if item in fridge:
        print("You have ", fridge[item], item)
    else:
        print(item, "is not in the fridge.")