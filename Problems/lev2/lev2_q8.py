#Chris Kopacz
#Python Exercises from Github
#Level 2, question 8
#created: 24 June 2017
"""
Question 8
Level 2

Question:
Write a program that accepts a comma-separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then the output should be:
bag,hello,without.world
"""


def main():

    userIn = input('Enter a comma-separated string of words:\n' + 
                   '>>> ')

    userIn = userIn.split(',')
    userIn.sort()

    result = ','.join(userIn)

    print(result)


if __name__ == "__main__":
    main()
