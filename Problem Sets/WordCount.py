# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(string):
    if(string==""):
        return 0
    count=1
    for i in range(0,len(string)):
        idx = string.find(" ")
        if(idx!=-1):
            count = count+1
            string = string[idx+1:]
    return count
        

passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)
#>>>56

