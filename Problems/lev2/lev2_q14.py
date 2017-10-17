#Chris Kopacz
#Python Exercises from Github
#Level 2, question 14
#created: 26 June 2017
"""
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculates the number of upper case letters
and lower case letters.

Suppose the following input is supplied to the program:
Hello world!

Then the output should be:
UPPER CASE 1
LOWER CASE 9
"""

#==============
#define main()
def main():
    upperCount = 0
    lowerCount = 0

    userIn = input('Enter a sentence:\n>>>')

    for iter in range(0,len(userIn)):
        if userIn[iter].isupper():
            upperCount += 1
        elif userIn[iter].islower():
            lowerCount += 1

    print('UPPER CASE ' + str(upperCount))
    print('LOWER CASE ' + str(lowerCount))


#============
#call main()
if __name__ == "__main__":
    main()
