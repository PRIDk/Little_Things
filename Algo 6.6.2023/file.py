def recurrency(n):
    if(n == 0):
        return 1
    else:
        recursion = recurrency(n-1) + 2 * n
        print(recursion)
        return recursion
    
recurrency(5)