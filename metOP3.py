from sympy import symbols, diff

a = 1
b = 1.5
e = 0.05
counter = 0

x = symbols('x')
skelet = 1/7 * x**7 - x**3 + 0.5 * x**2 - x
fun = diff(skelet, x)
print(fun)

while True:
    counter += 1
    aRes = fun.subs(x, a)
    bRes = fun.subs(x, b)
    xLine = a - (aRes / (aRes - bRes)) * (a - b)
    xLineRes = fun.subs(x, xLine)
    print("ШАГ №" + str(counter))
    print(aRes, bRes, xLine, xLineRes)
    if abs(xLineRes) <= e:
        print(xLine)
        print(1/7 * xLine**7 - xLine**3 + 0.5 * xLine**2 - xLine)
        print(counter)
        break
    else:
        if (xLineRes > 0):
            b = xLine
        else:
            a = xLine
