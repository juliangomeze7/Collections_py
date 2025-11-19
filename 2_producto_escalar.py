A = list(map(int, input("Lista A: ").split()))
B = list(map(int, input("Lista B: ").split()))
prod = sum(a * b for a, b in zip(A, B))
print("Producto escalar =", prod)
