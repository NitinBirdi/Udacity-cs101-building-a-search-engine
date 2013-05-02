# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.


def measure_udacity(s):
    i=0
    ct=0
    while(i<len(s)):
        if(s[i][0]=='U'):
            ct=ct+1
        i=i+1
    return ct

print measure_udacity(['Dave','Sebastian','Umika'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2