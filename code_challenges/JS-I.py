# Good morning! For today's code challenge, we're not going to write any functions. We'll be writing for-loops and console.log()'s. There are also a couple "self-study" questions for you.

# Press the "run" button. Initially, your console will look like this:
# ********** Exercise 1 of 4 **********

# ********** Exercise 2 of 4 **********

# ********** Exercise 3 of 4 **********

print('********** Exercise 1 of 4 **********')
unimaginativeArray = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# Write a "for" loop that console.log()'s the "zeroeth"
# value in the unimaginitiveArray, and thereafter every
# third value of the unimaginativeArray, i.e. 0, 3, 6,
# and 9: the zeroth, third, sixth, and ninth values.
# What is "zeroeth"? Has the word "first" become
# ambiguous now that I am a computer scientist? (Hint: yes).
for n in unimaginativeArray:
    if n%3 == 0:
        print(n)

print('\n********** Exercise 2 of 4 **********')
nameArray = [ 'Jacquelynn', 'Csaba', 'Ellen', 'Moises', 'Cole', 'Jeff', 'Dre\'Sean' ];
# Write a console.log() that displays the last value in
# nameArray. Use the `.length` property of array's
# to access the last value. What's going on with that
# slash in Dre'Sean's name?
print(nameArray[len(nameArray) - 1])

print('\n********** Exercise 3 of 4 **********')
adjectiveArray = [ 'awesome', 'fantastic', 'amazing', 'wonderful', 'fabulous', 'incredible', 'marvelous' ];
# Using both nameArray and adjectiveArray, make a
# "for" loop that console.log()'s a sentence for each
# corresponding value in the arrays. Use the string "is"
# to combine the name with the adjective. For example:
# "Jacquelynn is awesome"
# "Csaba is fantastic" et cetera...
for i in range(len(nameArray)):
    print(f"{nameArray[i]} is {adjectiveArray[i]}.")