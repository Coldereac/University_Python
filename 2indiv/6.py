n = int(input())
previous = int(n % 10)
n = int(n / 10)
current = int(n % 10)
n = int(n / 10)
increasing = True
while n > 0 and increasing:
    if previous < current:
        increasing = False
    else:
        previous = current
        current = int(n % 10)
        n = int(n / 10)
print("Зростає ", increasing)
