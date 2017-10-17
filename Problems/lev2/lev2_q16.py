#Chris Kopacz
#Python Exercises from Github
#Level 2, question 16
#created: 26 June 2017
"""
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a
sequence of comma-separated numbers.

Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9

Then the output should be:
1,9,25,49,81
"""

#==============
#define main()
def main():
    rList = []
    aList = []
    result = ''

    userIn = input('Enter comma-separated list of integers:\n>>>')

    aList = userIn.split(',')

    for iter in range(0,len(aList)):
        temp = int(aList[iter])
        if temp%2==1:
            rList.append(str(temp**2))

    result = ','.join(rList)

    print(result)
            

#===========
#call main()
if __name__ == "__main__":
    main()
