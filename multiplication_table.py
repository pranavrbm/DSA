def multi(n,i=1):
    # for i in range(1, 11):
    #     print("%d * %d = %d" % (n,i, n*i))
    if (i == 11):
        return 
    print(n, "*", i, "=", n * i)
    i+=1
    multi(n,i)
if __name__ == "__main__":
    n=3
    multi(n)