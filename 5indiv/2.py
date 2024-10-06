import numpy as np

n = 3
arr = np.random.randint(-5, 5, n * n)
print("Original = ", arr)

arr1 = np.reshape(arr, (n, n))
print("A0 = \n", arr1)

arr2 = np.pad(arr1, pad_width=1, constant_values=0)
print("A1 = \n", arr2)

randNums = np.random.randint(-10, 10, 5)
arr3 = arr2
arr3[2] = randNums
arr3[:, 2] = randNums
print("A2 = \n", arr3)

arr4 = arr3
arr4[:, 0] = 3
print("A3 = \n", arr4)