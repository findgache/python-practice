def factorialloop(f):
    result = 1
    for i in range(2,f+1):
        result *= i
        return result
print(factorialloop(6))