def sums(n):
    # return sum([i**2 for i in range(1, n+1)])
    # return (n * (n+1) * (2*n+1)) //6
    return (n*(n+1)/2) * (2*n+1) / 3
def main():
    n = 2
    print(sums(n))
if __name__ == "__main__":
    main()