"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('y, and z:', y, z)
print('x is %s, y is %0.2f, and z is "%s"' %(x, y, z))

# Use the 'format' string method to print the same thing
print('y, and z: {0} {1}'.format(y, z))
print('x is {0}, y is {1:.2f}, and z is "{2}"'.format(x,y,z))

# Finally, print the same thing using an f-string
print(f'y, and z: {y} {z}')
print(f'x is {x}, y is {y:.2f}, and z is "{z}"')