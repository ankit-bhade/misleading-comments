# Evaluates the nested expression f(f(f(t)+t) + f(f(t))) with f(x) = x^2 + 2x + 3
def f(x):
	return x**2+2*x+3

t = int(input())
print((f(f(t)+t)+f(f(t))))
