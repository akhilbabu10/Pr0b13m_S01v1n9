import string
def shift(x, key):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    n = []
    for i in x:
        if i.isupper() is True:
            n.append(upper[(upper.index(i)-key)%26])
        elif i.islower() is True:
            n.append(lower[(lower.index(i)-key)%26])
    return n
x= input("Enter encrypted string:")
key = int(input("Enter key:"))
print("".join(shift(x, key)))