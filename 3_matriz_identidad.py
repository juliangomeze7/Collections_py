n = int(input("n: "))
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(1 if i == j else 0)
    print(fila)
