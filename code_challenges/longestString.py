# Welcome REPL.it and code challenges at Lambda School!

# Write a function that takes an array of strings and return the longest string in the array.

strings = ('short', 'really, really long!', 'medium')
longest = ''
for string in strings:
    if len(string) > len(longest):
        longest = string

print(longest)