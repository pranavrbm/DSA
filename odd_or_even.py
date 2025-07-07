'''
Check whether a given number is even or odd

Given a number n, check whether it is even or odd. Return true for even and false for odd.

Examples: 

Input: n = 15
Output: false
Explanation: 15 % 2 = 1, so 15 is odd .

Input: n = 44
Output: true
Explanation: 44 % 2 = 0, so 44 is even.'''
def isEven(n):
    if (n & 1) == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    n=1
    if isEven(n):
        print("Even")
    else:
        print("Odd")
