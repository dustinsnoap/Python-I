# 3. Write a program to determine if a number, give on the command line, is prime.

#    1. How can you optimize this program?
#    2. Implement [The Sieve of
#       Erathosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
#       of the oldest algorithms known (ca. 200 BC).

import sys

num = int(sys.argv[1])
for n in range(2,num):
    if(num % n) == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")