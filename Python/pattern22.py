for  i in range(7):
    for j in range(7):
        if i == 0 or j ==0 or i ==6 or j ==6:
            print(4,end="")
        elif i ==1 or j == 1 or i ==5 or j==5:
            print(3,end="")
        elif i ==2 or j ==2 or i==4 or j==4:
            print(2,end="")
        elif i == 3 or j==3 :
            print(1,end="")
    print()
