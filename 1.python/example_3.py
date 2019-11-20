from timeit import timeit

random_small = """ 
import random
[random.randint(1, 10) for i in range(10)].sort()
"""
random_medium = """
import random
[random.randint(1, 100) for i in range(10000)].sort()
"""
random_large = """
import random
[random.randint(1, 10000) for i in range(100000)].sort()
"""



print("Tiempo para ordenar lista random pequeña: %.2f segundos." % timeit(random_small, number = 100))
print("Tiempo para ordenar lista random mediana: %.2f segundos." % timeit(random_medium, number = 100))
print("Tiempo para ordenar lista random grande: %.2f segundos." % timeit(random_large, number = 100))


