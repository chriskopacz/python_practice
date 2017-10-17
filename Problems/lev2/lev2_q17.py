#Chris Kopacz
#Python Exercises from Github
#Level 2, question 17
#created: 26 June 2017
"""
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based on a transaction
log from console input. The transaction log format is shown as follows:
D #
W #
e
D means deposit
W means withdrawal
E means end of log

Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
e

Then the output should be:
500
"""

#==============
#define main()
def main():
    net = 0;
    userIn = ''
    check = []

    print('Enter transactions:')

    while(True):
        userIn = input('>>> ')
        check = userIn.split(' ')

        if check[0] == 'D' or check[0] == 'd':
            net += int(check[1])
        elif check[0] == 'W' or check[0] == 'w':
            net -= int(check[1])
        else:
            break

    print('\nNet: ' + str(net))

#============
#call main()
if __name__ == "__main__":
    main()
