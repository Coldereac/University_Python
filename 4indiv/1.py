# %% Запис
from random import randint
import subprocess

L = set([randint(1, 9) for i in range(12)])
print(L)
T = tuple(zip(L, L))
print("Result in program: ")
print(T)
file = open("1.txt", "w")
file.write(str(T))
file.close()
result = subprocess.run(["cat", "1.txt"], stdout=subprocess.PIPE, text=True)
print("Result from file: ")
print(result.stdout)

#%% Отримання з файлу
file = open("1.txt", "r")
data = file.read().strip()
file.close()
pairs = eval(data)
print("Result of reading from file: ")
print(pairs)
