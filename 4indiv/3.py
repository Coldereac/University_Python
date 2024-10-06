import malynevskyi1

print("Through IDE")
print("First const = ", malynevskyi1.const1_1)
print("Second const = ", malynevskyi1.const1_2)
a = int(input("Input first number: "))  # 30, 20
b = int(input("Input second number: "))
print("First function = ", malynevskyi1.func1(a, b))
print("Second function = ", malynevskyi1.fibonacci(int(input("Input number for fibonacci func: "))))
print("\n\nTest from comand line: ")
import subprocess

process = subprocess.Popen(['python'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
commands = """
import malynevskyi1
print("First const = ", malynevskyi1.const1_1)
print("Second const = ", malynevskyi1.const1_2)
print("a = 300, b = 20")
print("First function = ", malynevskyi1.func1(300, 20))
print("n = 11")
print("Second function = ", malynevskyi1.fibonacci(11))
exit()
"""
stdout, stderr = process.communicate(commands)

# Виводимо результат команд
print("Output:")
print(stdout)
