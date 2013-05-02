# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

        
def add_to_index(index,keyword,url):
    temp=[]
    temp1=[]
    flag=0
    for x in index:
        if keyword in x:
            flag=1
            temp=x
            break
    
    if flag==0:
        temp.append(keyword)
        temp1.append(url)
        temp.append(temp1)
        index.append(temp)
    else:
        temp[1].append(url)
   
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
add_to_index(index,'udacity1','http://udacity.com')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


