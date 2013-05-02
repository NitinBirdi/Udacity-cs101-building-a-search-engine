# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    temp=[]
    for x in index:
        if keyword in x:
            return x[1]
    
    return temp





print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']