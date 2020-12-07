"""
    REAl Zeros
"""


"""
Example: 

def g(x): 
	return 1/x+2.5	#apenas a raiz positiva

def f(x): 
	return 2*x*x-5*x-2
"""


def picard_peano(x, max_iter, fn):
	for i in range(max_iter):
		x = fn(x)
		print(x)


# picard_peano(3, 20, g)