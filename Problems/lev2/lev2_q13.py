#Chris Kopacz
#Python Exercises from Github
#Level 2, question 13
#created: 26 June 2017
"""
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculates the number of letters and digits.

Suppose the following in put is supplied to the program:
hello world! 123

Then the output should be:
LETTERS 10
DIGITS 3
"""

#==============
#define main()
def main():
    letterCount = 0
    digitCount = 0

    userIn = input("Enter a sentence:\n>>>")

    for iter in range(0,len(userIn)):
        if userIn[iter].isalpha():
            letterCount += 1
        elif userIn[iter].isdigit():
            digitCount += 1
    
    print('LETTERS ' + str(letterCount))
    print('DIGITS ' + str(digitCount))


#============
#call main()
if __name__ == "__main__":
    main()
