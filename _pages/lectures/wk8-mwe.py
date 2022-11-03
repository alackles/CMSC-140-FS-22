instring = "hello world"
outstring = ""
string_list = instring.split(" ")
for i in range(len(instring)):
    if instring[i] == " ":
        break
    if i % 2:
        outstring += instring[i].upper()
    else:
        outstring += instring[i].lower()
print(outstring)