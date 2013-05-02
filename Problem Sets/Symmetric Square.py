# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(l):
   temp=[]
    
   if l==[]:
        return True
   if not len(l[0])==len(l):
        return False
    
   for i in range(0,len(l[0])):
        t=[]
        for j in range(0,len(l)):
            t.append(l[j][i])
        temp.append(t)
   
   if l==temp:
       return True
   else:
       return False

#print symmetric([[1, 2, 3],
#                [2, 3, 4],
#               [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#              ["dog", "dog", "fish"],
#               ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3]])
#>>> False