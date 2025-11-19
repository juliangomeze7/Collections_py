notas = {}
while True:
    dato = input("Nombre y nota (fin para terminar): ")
    if dato.lower() == "fin":
        break
    nombre, nota = dato.split()
    notas[nombre] = float(nota)
print("Promedio general:", sum(notas.values())/len(notas))
