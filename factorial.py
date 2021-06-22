# Factorial of a Large Number

def factorialWithoutRecusrion(n):
    fact=1
    for i in range(1,n+1):
        fact*=i

def factorialRecursion(n):
    if n == 0:
        return 1
    
    return n * factorialRecursion(n-1)

num = 5
factorialRecursion(num)
factorialWithoutRecusrion(num)
