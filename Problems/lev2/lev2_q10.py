#Chris Kopacz
#Python Exercises from Github
#Level 2, question 10
#created: 26 June 2017
"""
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as inptut and
prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the ouput should be:
again and hello makes perfect practice world
"""

def removeDoubles(aList):
    
    i = 0
    result = ''

    while(i<len(aList)):
        if aList.count(aList[i]) != 1:
            aList.pop(i)
        else:
            i += 1

    result = ' '.join(aList)

    return result
#=======


def main():
    result = ''

    userIn = input('Enter a string containing whitespace separated words:\n'
                   '>>> ')

    strList = userIn.split(' ')
    strList.sort()
    
    result = removeDoubles(strList)

    print(result)


#==========
#call main()
if __name__ == "__main__":
    main()
