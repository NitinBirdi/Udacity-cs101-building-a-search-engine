# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    ht = []
    while nbuckets>0:
        ht.append([])
        nbuckets -= 1
    return ht
