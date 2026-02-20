'''
Sum of Digits of a Number

Given a number n, find the sum of its digits.

Examples : 

Input: n = 687
Output: 21
Explanation: The sum of its digits are: 6 + 8 + 7 = 21

Input: n = 12
Output: 3
Explanation: The sum of its digits are: 1 + 2 = 3'''
def sum_of_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_of_digits( n // 10)
def main():
    n = 12345
    print(sum_of_digits(n))
if __name__ == "__main__":
    main()
