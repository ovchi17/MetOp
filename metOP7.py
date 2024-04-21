import sympy as sp
import math

e = 0.0005

X = 0
Y = 0
Z = 0
pX = 2 * X + 12 * Y
pY = 2 * Y + 12 * X
pZ = 2 * Z + 2

while True:
    h = sp.Symbol('h')
    func = (X - h * pX)**2 + (Y - h * pY)**2 + (Z - h * pZ)**2 + 12 * (X - h * pX) * (Y - h * pY) + 2 * (Z - h * pZ)
    derivative = sp.diff(func, h)
    solution = sp.solve(derivative, h)
    hResult = solution[0]
    X = X - hResult * pX
    Y = Y - hResult * pY
    Z = Z - hResult * pZ
    pX = 2 * X + 12 * Y
    pY = 2 * Y + 12 * X
    pZ = 2 * Z + 2
    if math.sqrt(pX**2 + pY**2 + pZ**2) <= e:
        break
print(X, Y, Z)
print(X**2 + Y**2 + Z**2 + 12 * X * Y + 2 * Z)