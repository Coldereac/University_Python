from malynevskyi2 import *

print("All functions from 2 module: ")
print("Func1: ", func1(1))
print("Func2: ", func2(4))
print("Func3: ", func3(1 + 1j))
print("Func4: ", func4(4))
print("Func5: ", func5(5))
print("Func6: ", func6(6))
print("Func7: ", func7(7))

from malynevskyi3 import *

print("All functions from 3 module: ")
print("Half div 1x: ", half_div(func1, 0, 2, 0.0001))
print("Half div 2x: ", round(half_div(func1, -4, -3, 0.0001), 3))
print("Writing list into file")
func([2, 540, 999, 100, -20, 40], "test.txt")
import subprocess
result = subprocess.run(['cat', 'test.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("Result from file: ", result.stdout)
