# Good morning! Complete the function so that it converts dash-delimited ("kebab" case) & underscore-delimited ("snake" case) words into "camel" casing. The first word within the output should be capitalized only if the original word was capitalized.

# toCamelCase("the-stealth-warrior")
# // returns "theStealthWarrior"
# toCamelCase("The_stealth_warrior")
# // returns "TheStealthWarrior"

def toCamelCase(string):
    newstr = ""
    upper = False
    for c in string:
        if upper:
            c = c.upper()
            upper = False
        if c == '-':
            upper = True
        else:
            newstr = newstr + c
    return newstr

print(toCamelCase("the-stealth-warrior"))