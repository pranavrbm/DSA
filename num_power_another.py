'''
Check if a number is a power of another number
Last Updated : 05 Jun, 2025
Given two positive numbers x and y, check if y is a power of x or not.
Examples :
Input:  x = 10, y = 1
Output: True
x^0 = 1

Input:  x = 10, y = 1000
Output: True
x^3 = 1

Input:  x = 10, y = 1001
Output: False
'''


def isPower(x, y):
    if x == 1:
        return y == 1
    pow = 1
    while pow < y:
        pow *= x

    return y == pow


if __name__ == "__main__":
    print(isPower(10, 1))
    print(isPower(1, 10))
    print(isPower(2, 128))
