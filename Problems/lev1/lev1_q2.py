#Chris Kopacz
#Python Exercises from Github
#Level 1, question 2
#created: 20 June 2017
"""
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""

a = 0
result = 1
userIn = input("Enter a number: ")

try:
    a = int(userIn)
    if a >0:
        for iter in range(1,a+1):
            result *= iter
        print(str(result))
    elif a == 0:
        print('1')
    else:
        print("no")
except ValueError:
    print("Not a number")
