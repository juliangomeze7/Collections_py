A = eval(input("Matriz: "))
trans = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print(trans)
