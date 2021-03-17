Parzysta = []
i = 0
print("Podaj 10 liczb: \n")
while i < 10:
    a = input()
    a = int(a)
    if a%2==0:
        Parzysta.append(a)
    i+=1
print(Parzysta)
print("\n")