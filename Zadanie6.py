print("Podaj 3 liczby: \n")
a = input()
b = input()
c = input()
print("Najwieksza liczba to: ")
if (a>=b) & (a>=c):
    print(a)
elif (b>=a) & (b>=c):
    print(b)
else:
    print(c)
print("\n")