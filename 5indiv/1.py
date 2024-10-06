
import numpy as np

n = int(input("Enter size of array: "))
arr = np.random.randint(-10, 10, n)
print(arr)

arr1 = arr[::2][arr[::2] > 0]

arr2 = arr[1::2][arr[1::2] > 0]

arr3 = arr[arr <= 0]

arr = np.concatenate((arr1, arr2, arr3))

print(arr)
