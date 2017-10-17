#Chris Kopacz
#Python Exercises from Github
#Level 2, question 11
#created: 26 June 2017
"""
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as
its input and then check whether they are divisible by 5 or not. The numbers that are
divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
"""

def checkValues(numList):
    pList = []

    for iter in range(0,len(numList)):
        temp = int(numList[iter],2)
        if temp%5 == 0:
            pList.append(numList[iter])

    return pList
#=========

#define main()
def main():
    result = ''

    userIn = input('Enter a comma separated list of 4 digit binary numbers:\n' +
                   '>>> ')

    aList = userIn.split(',')

    rList = checkValues(aList)

    if len(rList)==1:
        print(rList[0])
    elif len(rList)==0:
        print('None')
    else:
        result = ','.join(rList)
        print(result)

#==========
#call main()
if __name__ == "__main__":
    main()
