# Benjamin Graham valor intrinseco de la accion

EPS = float(input("Beneficio neto por accion: "))
G = float(input("Crecimiento anual esperado del beneficio neto durante los pŕoxios 10 años: "))
TNX = float(input("Treasury Yield 10 Years: "))
MS = float(input("Margen de Seguridad: "))
# Formula
V = EPS * (8.5+2*G)*TNX*MS
print(V)

# Calculo Multiplicador de beneficio anual en tasa de crecimiento previstas,
# basadas en la formula simplificada de Benjamin Graham
# tabla 11.4 , pagina 295, Libro Inversor Inteligente de Benjamin Graham

G = float(input("Crecimiento anual esperado del beneficio neto durante los pŕoxios 10 años: "))
M = float(input("Temporalidad de la tasa de crecimiento en Unidad Años: "))
N = float(input("Temporalidad Final en Unidad Años: "))
# fOrmula
GN = ((1+G))**(M/N)-1)*100
print(GN)
