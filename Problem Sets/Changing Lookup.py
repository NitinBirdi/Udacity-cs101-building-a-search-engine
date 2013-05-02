# Change the lookup procedure
# to now work with dictionaries.

def lookup(index, keyword):
    if keyword in index:
            return index[keyword]
    return None
