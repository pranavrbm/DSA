'''
Write a program to reverse digits of a number
Given an Integer n, find the reverse of its digits.

Examples:  

    Input: n = 122
    Output
    Explanation: By reversing the digits of number, number will change into 221.

    Input: n = 200
    Output: 2
    Explanation: By reversing the digits of number, number will change into 2.

    Input: n = 12345 
    Output: 54321
    Explanation: By reversing the digits of number, number will change into 54321.
'''
n = 100123
rev = 0
while n != 0:
    a = n % 10
    rev = rev * 10 + a
    n //= 10
print(rev)
