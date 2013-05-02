#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    current = 0
    after = 1
    for i in range(0,n):
        current,after = after,current+after
    return current

print fibonacci(36)
#>>> 14930352