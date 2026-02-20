'''
Find the number closest to n and divisible by m

Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

Examples: 

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the closest to 13, divisible by 4.

Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.'''

# def num_closest_to_n(n,m):
#     min_difference=float("inf")
#     closest=0
    
#     for i in range(n-abs(m), n+abs(m)+1):
#         if i % m == 0:
#             difference = abs(n-i)
#             if difference < min_difference or (difference == min_difference and abs(i) > abs(closest)):
#                 closest=i
#                 min_difference= difference
#     return closest 

def num_closest_to_n(n,m):
    q=int(n/m)
    n1=m*q
    if (n*m) < 0:
        n2=m*(q+1)
    else:
        n2=m*(q-1)
    if abs(n-n1) < abs(n-n2):
        return n1 
    return n2
  
if __name__ == "__main__":
    n=13 
    m=4
    print(num_closest_to_n(n, m))  # Output: 12

