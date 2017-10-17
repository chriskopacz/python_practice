#Chris Kopacz
#Python Exercises from Github
#Level 2, question 7
#created: 24 June 2017
"""
Question 7
Level 2

Question:
Write a program which takes two digits, X and Y, as input and generates a 2-dimensional
array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1,...,X-1; j=0,1,...Y-1
Example:
SUppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0,], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""


def main():

    arrayX = []
    result = []

    userX = input('Enter X value:  ')
    userY = input('Enter Y value:  ')

    for iter in range(0,int(userX)):
        arrayX = []
        for jter in range(0,int(userY)):
            arrayX.append(iter*jter)

        result.append(arrayX)

    print(result)


if __name__ == "__main__":
    main()
