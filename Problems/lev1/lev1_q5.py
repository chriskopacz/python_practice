#Chris Kopacz
#Python Exercises from Github
#Level 1, question 5
#created: 21 June 2017
"""
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case
Also please include simple test function to test the class methods
"""

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        aStr = self.s.upper()
        print(aStr)

#test functions
#define main function
def main():
    aString = InputOutString()
    aString.getString()
    aString.printString()

#call main function
if __name__ == "__main__":
    main()
