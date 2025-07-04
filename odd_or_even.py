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
