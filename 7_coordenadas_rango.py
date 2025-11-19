x, y = map(int, input("Coordenada x y: ").split())
a, b = map(int, input("Rango (min max): ").split())
print("Dentro del rango" if a <= x <= b and a <= y <= b else "Fuera del rango")
