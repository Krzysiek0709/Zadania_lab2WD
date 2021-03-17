import sys as system


system.stdout.write("Podaj 3 liczby: ")
x = system.stdin.readline()
y = system.stdin.readline()
z = system.stdin.readline()
x = int(x)
y = int(y)
z = int(z)
print(pow(x, y) + z)
print("\n")