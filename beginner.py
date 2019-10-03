# Beginner function(s)
## Code Attribution: Code snippets taken and adapted from https://towardsdatascience.com/how-to-be-pythonic-and-why-you-should-care-188d63a5037e

def sum_of_a_range(a = 10,b = 1000):
    """ 
    What the heck is a docstring?!?
    """
    total_sum = 0
    for i in range(a, b):
        total_sum += i
    return total_sum
