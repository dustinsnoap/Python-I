# Good morning! Write a function that takes in a string, reverses the 'casing' of that string, and returns the "reversed-casing" string.

# const string = 'HELLO world!';
# console.log(reverseCase(string)); // <--- hello WORLD!

def reverseCase(string):
    newstr = ""
    for c in string:
        if c.isupper(): newstr = newstr + c.lower()
        elif c.islower(): newstr = newstr + c.upper()
        else: newstr = newstr + c
    return newstr

print(reverseCase("HELLO world!"))