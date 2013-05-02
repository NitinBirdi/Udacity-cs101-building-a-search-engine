# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(l):
    if l==[]:
        return 0
    return max(l)



print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
