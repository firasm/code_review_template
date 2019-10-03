# Jarome's Edit
# Beginner function(s)
## Code Attribution: Code snippets taken and adapted from https://towardsdatascience.com/how-to-be-pythonic-and-why-you-should-care-188d63a5037e

def sum_of_a_range(a=10,b=1000):
    """ 
   Adds the numbers between a and b
   
   a -- a number
   b -- a number
   
   examples:
   sum_of_a_range(0,2)
    """

	total_sum = 0
	while b >= a:
	    total_sum += a
	    a += 1

	return total_sum
