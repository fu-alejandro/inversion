# Gestion de Riesgo: Formula de Larry Williams para calculo lote, accion, contrato
# por operacion

K = float(input("Capital: "))
R = float(input("Porcentaje de Riesgo: "))
E = float(input("Entrada: "))
SL = float(input("Stop Loss: "))
# Formula
L = (K * R / 100)/(E-SL)
print(L)
