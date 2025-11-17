char=["A","B","C","D","E"]
for i in range(6):
    for j in range(i,0,-1):
        print(char[-j],end="")
    print()
