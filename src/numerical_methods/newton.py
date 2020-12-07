"""
    REAl Zeros
"""


"""
Example: 

def f(x): 
	return 2*x*x-5*x-2
def df(x): 
	return 4*x-5
"""

def newton(x, max_iter, f, df):
    for i in range(max_iter):
        x = x - f(x) / df(x)
        print(x)

# newton(3, 20, f, df)