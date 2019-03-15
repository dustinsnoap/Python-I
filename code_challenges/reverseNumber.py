# Good morning! Write a function called reverseNumber that reverses a number.

# Input Example: 
# 12345
# 555

# Output Example:  
# 54321
# 555

def reverse(num):
    newNum = ''
    for n in str(num):
        newNum = n + newNum
    return int(newNum)

print(reverse(12345))