'''
Happy Numbers - A happy number is defined by the following process. Starting with any positive integer,
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers, 
while those that do not end in 1 are unhappy numbers. 
Display an example of your output here. Find first 8 happy numbers.
'''

def happy_number(n):
    n1 = sum([int(letter) ** 2 for letter in str(n)])
    happy = [n, n1]
    while n1 != 1:
        n1 = sum([int(letter) ** 2 for letter in str(n1)])
        if n1 in happy:
            return None
        happy.append(n1)

    return happy


print(happy_number(7))
