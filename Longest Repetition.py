# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(l):
    if len(l)>0:
        prev = l[0]
        curr = l[0]
        maxi,ct=0,0
        for x in l:
            if x == prev:
                ct+=1
            else:
                if ct>maxi:
                    maxi = ct
                    curr = prev
                prev = x
                ct=1
            
        if ct>maxi:
            curr = x
        return curr


#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([2, 2, 3, 3, 3])
# 3

print longest_repetition([])
# None

