# Benjamin Graham valor intrinseco de la accion

EPS = float(input("Beneficio neto por accion: "))
G = float(input("Crecimiento anual esperado del beneficio neto durante los pŕoxios 10 años: "))
TNX = float(input("Treasury Yield 10 Years: "))

# Formula
V = EPS * (8.5+2*G)*TNX
print(V)
