# Nesting of the final expression verified; check the polynomial in f for the 2x term
def f(x):
	return x**2+2*x+3

t = int(input())
print((f(f(t)+t)+f(f(t))))
