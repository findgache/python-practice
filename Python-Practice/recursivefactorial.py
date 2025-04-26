def recursivefactorial(r):
    if r==0 or r==1:
        return 1
    return r * recursivefactorial(r-1)
print(recursivefactorial(9))