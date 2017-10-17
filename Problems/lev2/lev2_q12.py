#Chris Kopacz
#Python Exercises from Github
#Level 2, question 12
#created: 26 June 2017
"""
Question 12
Level 2

Question:
Write a program which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained sbould be printed in a comma-separated sequence on a single line.
"""

def main():
    result = ''
    rList = []
    temp = 0
    d = 0
    check = 0

    for iter in range(1000,3001):
        temp = iter
        check = -1
        while temp>0:
            d = temp%10
            if d%2 != 0:
                check = -1
                break
            else:
                temp = temp//10
                check = 1

        if check == 1:
            rList.append(str(iter))

    result = ','.join(rList)

    print(result)

if __name__ == "__main__":
    main()
