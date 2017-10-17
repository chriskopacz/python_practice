#Chris Kopacz
#Python Exercises from Github
#Level 2, question 6
#created: 24 June 2017
"""
Question 6
Level 2

Question:
Write a program that calculates and printes the value according to the given formula:
Q = sqrt[(2*C*D)/H]
Following are the fixed values of C and H:
C=50 H=30
D is the variable whose values chould be input to your program in a comma-
separated sequence.
Example:
Let us assume the following comma-separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

def aFunc(d):
    c = 50
    h = 30

    result = int(((2*c*d)/h)**.5)

    return result
#==========

def main():

    result = ''

    userIn = input('Enter integer values as a comma-separated string:\n')

    userIn = userIn.split(',')

    for iter in range(0,len(userIn)):
        temp = aFunc(int(userIn[iter]))

        result = result + str(temp) + ','

    result = result.rstrip(',')
    print(result)


if __name__ == "__main__":
    main()
