#Write a python function which accepts three numbers and returns True if
#a. one of the three numbers is "close" to any one of the other numbers (differing from a number by at most 1), and
#b.Number that is left out is "far", differing from both other values by 2 or more.
#Return false if the above mentioned conditions are not satisfied.

def close_number(num1,num2,num3):
    #start writing your code here
    if num1 - num2 != 1 or num1 - num3 != num1:
    if num1 - num2 <= 2:
        return False
    else:
        return True
    
    
    
print(close_number(5,4,2))
