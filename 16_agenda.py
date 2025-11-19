agenda = {}
while True:
    n = input("Nombre: ")
    if n.lower() == "fin":
        break
    t = input("Teléfono: ")
    agenda[n] = t
print(agenda)
