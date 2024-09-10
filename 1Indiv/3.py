import math

a = float(input('a= '))
b = float(input('b= '))
z1 = math.fabs((a - b) * math.sqrt((a + b) / (a - b)) + a - b)
z2 = math.fabs((a - b) * (math.sqrt((a + b) / (a - b)) - 1))
print("Отримано: ", z1 * z2)

print("Очікувалося: ", 8)