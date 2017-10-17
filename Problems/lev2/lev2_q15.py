#Chris Kopacz
#Python Exercises from Github
#Level 2, question 15
#created: 26 June 2017
"""
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with 'a' being a digit supplied
by the user.

Suppose the following input is applied to the porgram:
9

Then, the output should be:
11106
"""

#==============
#define main()
def main ():
    result = 0
    n = 0

    userIn = input('Enter an integer digit:\n>>>')

    #a
    n = int(userIn)
    result += n

    #aa
    result += (10*n + n)

    #aaa
    result += (100*n + 10*n + n)

    #aaaa
    result += (1000*n + 100*n + 10*n + n)

    print(str(result))

#============
#call main()
if __name__ == "__main__":
    main()
