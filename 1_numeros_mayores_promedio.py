nums = list(map(float, input("Ingrese números separados por espacio: ").split()))
prom = sum(nums) / len(nums)
mayores = [n for n in nums if n > prom]
print("Promedio:", prom)
print("Mayores que el promedio:", mayores)
