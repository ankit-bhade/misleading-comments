# Evaluates f(f(t)+t) + f(f(t)), the combined value of the two nested branches of f
def f(x):
	return x**2+2*x+3

t = int(input())
print((f(f(t)+t)+f(f(t))))
