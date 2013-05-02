# Two Gold Stars
# Question 2: Combatting Link Spam

# One of the problems with our page ranking system is pages can 
# collude with each other to improve their page ranks.  We consider 
# A->B a reciprocal link if there is a link path from B to A of length 
# equal to or below the collusion level, k.  The length of a link path 
# is the number of links which are taken to travel from one page to the 
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A, 
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link 
# A->B, which includes one link and so is of length 1. (it requires 
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to 
#   - take an extra input k, which is a non-negative integer, and 
#   - exclude reciprocal links of length up to and including k from 
#     helping the page rank.


def is_reciproval(graph, origin, current, depth):
	#print 'is_reciproval =', origin, current, depth	
	if depth <= 0:
		if origin == current:
			return True
		else:
			return False

	#print 'current =', current, 'link =', graph[current]
	for node in graph[current]:
		if is_reciproval(graph, origin, node, depth-1):
			return True
	return False

def compute_ranks(graph, k):
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_reciproval(graph, node, page, k):
                    	newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

#print compute_ranks(g, 0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

#print compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

#print compute_ranks(g, 2)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}

