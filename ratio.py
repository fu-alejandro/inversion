# Ratio P/FCF Price to Free Cash Flow, resultado flojo de caja, mide las veces del tamaño del capital sobre el flujo de caja.
P = float(input("Market Capitalization: "))
FCF = float(input("Free Cash Flow: "))
R = P / FCF
print(R)

# Ratio PE o PER Price Earning Ratio, Resultado son los años para recuperar el capital o inversion.
P = float(input("Market Value per share: "))
E = float(input("Earning per share: "))
R = P / E
print(R)

# Ratio ROE Return on Equity, Resultado porcentaje anual para recuperar el capital o inversion.
E = float(input("Beficio: "))
K = float(input("Capital: "))
R = E / K
print(R)

# Ratio Debt / Equit,
D = float(input("Total Liabilities: "))
Q = float(input("Total share holders: "))
R = D / Q
print(R)

# Ratio Sales
P = float(input("Market Value per share: "))
E = float(input("Earning per share: "))
R = P / E
print(R)
