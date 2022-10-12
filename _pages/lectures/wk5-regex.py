import re

emails = ['acacia.ackles@lawrence.edu',
    'scott.corry@lawrence.edu',
    'deanna.donohue@lawrence.edu',
    'mmore500@msu.edu',
    '2484ythsgkd@lawrence.edu',
    'scams_are_cool@lawrence.edu',
    'elizabeth.k.sattler@lawrenc.edu',
    'acacia@lawrence.edudjkdgkdk']

# Idea 1:

print("Split:")
for email in emails:
    e = email.split('@')
    if (e[1] == "lawrence.edu"):
        print(email, "is Valid")

print("In:")
for email in emails:
    if "@lawrence.edu" in email:
        print(email, "is Valid")

print("Endswith:")
for email in emails:
    if email.endswith("@lawrence.edu"):
        print(email, "is Valid")

def isValidFile(string):
    return string.endswith(".py") or string.endswith(".pdf")

def isValidFile_regex(string):
    regex = re.compile(r'[A-Za-z0-9]+\.(py|pdf)$')
    return re.search(regex, string)

print(isValidFile_regex("hello.py"))
print(isValidFile_regex("hello.py.cpp"))


condition = True

def newfunction(condition):
    if condition:
        return True
    else:
        return False

def newfunction(condition): # return true when condition true
    return condition


def isEven(num):
    if num % 2 == 1:
        return False
    else:
        return True

def isEven(num):
    return not num % 2 == 1

def newfunction(condition): # return false when condition true
    return not condition


def check_app(string):
    return "app" in string and not string.startswith("app")

# . = any character
# + = 1 or more times
# * = 0 or more time

# tell python what regex we want

print("regex:")
email_regex = re.compile(r'[a-z]+\.([a-z]+.)?[a-z]+@lawrence\.edu$')
for email in emails:
    if re.search(email_regex, email):
        print(f"{email} is a valid address.")

