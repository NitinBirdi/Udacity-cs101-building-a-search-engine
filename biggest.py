# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        return num1
    else:
        if (num2>num1) and (num2>num3):
            return num2
        else:
            return num3




print biggest(3, 16, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9