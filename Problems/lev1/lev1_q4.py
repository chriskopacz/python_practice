#Chris Kopacz
#Python Exercises from Github
#Level 1, question 4
#created: 21 June 2017
"""
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and 
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

userIn = input("Enter a list of numbers, separated by commas, no spaces:\n" +
              ">>>")

aList = []
aTuple = 0

aList = userIn.split(',')
aTuple = tuple(aList)

print("List:")
print(aList)
print("Tuple:")
print(aTuple)
