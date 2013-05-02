# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'


def is_friend(name):
    if name[0] == 'D':
        return 1
    else:
        return 0



print is_friend('Diane')
#>>> True

print is_friend('Fred')
#>>> False