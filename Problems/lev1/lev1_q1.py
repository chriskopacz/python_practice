#Chris Kopacz
#Python Exercises from Github
#Level 1, question 1
#created: 20 June 2017
"""
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a 
multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

aList = []
min = 2000
max = 3200

for iter in range(min, max+1):
    if iter%7==0 and iter%5!=0:
        #aList.append(iter)
        aList.append(str(iter))

#print(aList)
print(','.join(aList))
