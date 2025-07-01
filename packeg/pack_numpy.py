import numpy as np

list_biasa = [1,2,3,4,5]
list_numpy_a = np.array([1,2,3,4,5])

# print(f"List biasa = {list_biasa}")
print(f"List dengan numpy = {list_numpy_a}")

# experimen untuk matrix
print(f"List dengan numpy = {list_numpy_a**2}")

# experiment matrix (list di dalam list)
list_numpy_b = np.array([(1,2), (3,4)])
print(f"List dengan numpy = \n{list_numpy_b}")
print(f"List dengan numpy = \n{list_numpy_b**2}")

nummpy_zero = np.zeros((1,2))
print(nummpy_zero)

nummpy_ones = np.ones((1,2))
print(nummpy_ones)

print("="*20)

jumplah_numpy = nummpy_ones + list_numpy_b**2
print(jumplah_numpy)