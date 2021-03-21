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
  
    return false; 
  
  
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
