# Good morning! Write a function called reverseString that accepts a string and returns a reversed copy of the string.

# Input Example:
# 'hello world'
# 'asdf'
# 'CS rocks!'

# Output Example:
# 'dlrow olleh'
# 'fdsa'
# '!skcor SC'

def reverse(str):
    reversed = ''
    for c in str:
        reversed = c + reversed
    return reversed

print(reverse("Sir, I demand, I am a maid named Iris"))