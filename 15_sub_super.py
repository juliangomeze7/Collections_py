A = eval(input("A: "))
B = eval(input("B: "))
if A.issubset(B):
    print("A es subconjunto de B")
if B.issuperset(A):
    print("B es superconjunto de A")
