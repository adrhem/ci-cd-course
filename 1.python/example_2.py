def factorial(n):
    if n < 1: 
        raise ValueError("N tiene que ser mayor a 1")
    elif n <= 2:
        return n
    else:
        return n * factorial(n - 1)
limit = 10
stop_in = -1
increment = -1

for n in range(limit, stop_in, increment):
    print("Factorial de %s es %s" % (n, factorial(n)))