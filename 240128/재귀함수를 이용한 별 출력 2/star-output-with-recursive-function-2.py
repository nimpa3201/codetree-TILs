n = int(input())

def printStar(k):
    if k ==0:
        
        return
    else:
        print("* "*k)
        printStar(k-1)
        print("* "*k)
printStar(n)