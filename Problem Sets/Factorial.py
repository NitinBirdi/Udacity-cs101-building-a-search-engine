# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    a = 1
    while n > 1:
        a = a * n
        n = n-1
    
    return a



print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

