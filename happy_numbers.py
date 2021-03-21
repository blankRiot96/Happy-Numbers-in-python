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

# python program to check if a number 
# is happy number 
  
  
# Returns sum of squares of digits 
# of a number n. For example for n = 12 
# it returns 1 + 4 = 5 
def sumDigitSquare( n): 
    sq = 0; 
    while (n!=0): 
        digit = n % 10
        sq += digit * digit 
        n = n // 10
          
    return sq; 
  
  
# Returns true if n is Happy number 
# else returns false. 
def isHappy(n): 
    # A set to store numbers during 
    # repeated square sum process 
    s=set() 
    s.add(n) 
  
    # Keep replacing n with sum of 
    # squares of digits until we either 
    # reach 1 or we endup in a cycle 
    while (True): 
  
        # Number is Happy if we reach 1 
        if (n == 1): 
            return True; 
  
        # Replace n with sum of squares 
        # of digits 
        n = sumDigitSquare(n) 
  
        # If n is already visited, a cycle 
        # is formed, means not Happy 
        if n in s: 
            return False
  
        # Mark n as visited 
        s.add(n) 
  
    return False; 
  
  
# Driver code 
  
run = True
n = 0
count = 0
while run:
    n += 1
    if (isHappy(n)): 
        happy = True
        print(n)
        count += 1
    else: 
        happy = False
    if count == 8:
        run = False
