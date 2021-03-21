
def happy_number(n):
    n1 = sum([int(letter) ** 2 for letter in str(n)])
    happy = [n, n1]
    while n1 != 1:
        n1 = sum([int(letter) ** 2 for letter in str(n1)])
        if n1 in happy:
            return None
        happy.append(n1)

    return happy

#isHappyNumber() will determine whether a number is happy or not    
def isHappyNumber(num):   
    count2 = 0;  
    while True and count2 <= 8:
        rem = sum = 0;    
            
        #Calculates the sum of squares of digits    
        while(num > 0):    
            rem = num%10;    
            sum = sum + (rem*rem);    
            num = num//10;    
        return sum;    

    num += 1;  
    result = num;    
        
    while(result != 1 and result != 4):    
        result = isHappyNumber(result);    
        
    #Happy number always ends with 1    
    if(result == 1):    
        print(str(num) + " is a happy number");    
        count2 += 1; 
    #Unhappy number ends in a cycle of repeating numbers which contain 4    
    elif(result == 4):    
        print(str(num) + " is not a happy number");  

print(happy_number(7))
print(isHappyNumber(1))
