#Chris Kopacz
#Python Exercises from Github
#Level 1, question 3
#created: 20 June 2017
"""
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains 
(i, i*i) such that is an integral number between 1 and n (both included). and then the 
program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

a = 0
aList = []
aDict = {}
userIn = input("number: ")

try:
    a = int(userIn)
    if a > 0:
        for iter in range(0,a):
            aList.append([(iter+1),(iter+1)**2])
    elif a == 0:
        aList.append([0,0])
    else:
        print("no")

    aDict = dict(aList)
    print(aDict)
except ValueError:
    print("no")

