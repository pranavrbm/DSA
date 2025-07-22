'''
Check whether triangle is valid or not if sides are given
Given three sides, check whether triangle is valid or not. 

Examples:  

Input :  a = 7, b = 10, c = 5 
Output : Valid
We can draw a triangle with the given three edge lengths.

Input : a = 1, b = 10, c = 12 
Output : Invalid
We can not draw a triangle with the given three edge lengths.
'''

def isTriange(a:int,b:int,c:int) -> bool:
    if (a+b<=c) or (a+c<=b) or (b+c<=a):
        return False
    else: 
        return True

a,b,c= map(int, input().split())
tri=isTriange(a,b,c)
print("Tringle" if tri else "not")

    
