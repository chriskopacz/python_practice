#Chris Kopacz
#Python Exercises from Github
#Level 3, question 18
#created: 26 June 2017
"""
Question 18
Level 3

Question:
A website requires users to input username and password to register. Write a program to
check the validity of passwords input by users.
Following are the criteria for checking the password:
1. At least one letter between [a-z]
2. At least one number between [0-9]
3. At least one letter between [A-Z]
4. At least one character from [$#@]
5. Minimum length of 6 characters
6. Maximum length of 12 characters
Your program should accept a sequence of comma-separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed,
each separated by a comma.
Example:
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then the output should be:
ABd1234@1
"""

import re

#==================
#define checkPass()
def checkPass(a):
    if len(a)>=6 and len(a)<=12:
        if re.search("[a-z]",a):
            if re.search("[0-9]",a):
                if re.search("[A-Z]",a):
                    if re.search("[$#@]",a):
                        return a
                    else:
                        return '0'
                else:
                    return '0'
            else:
                return '0'
        else:
            return '0'
    else:
        return '0'

    
#==============
#define main()
def main():
    
    passList = []
    returnList = []
    validList = []
    result = ''

    userIn = input('Enter a list of comma-separated passwords:\n>>> ')

    passList = userIn.split(',')
    
    for iter in range(0,len(passList)):
        returnList.append(checkPass(passList[iter]))

    for iter in range(0,len(returnList)):
        if returnList[iter] != '0':
            validList.append(returnList[iter])

    if len(validList) > 1:
        result = ','.join(validList)
        print(result)
    elif len(validList)==1:
        result = validList[0]
        print(result)
    else:
        result = 'None'
        print(result)
        

#===========
#call main()
if __name__ == "__main__":
    main()
