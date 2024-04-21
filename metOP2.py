a = 1
b = 1.5
e = 0.05
counter = 0


x1 = a + 0.382 * (b - a)
x2 = a + 0.618 * (b - a)

while abs(b - a) >= e:
    counter += 1
    y1 = 1/7 * x1**7 - x1**3 + 0.5 * x1**2 - x1
    y2 = 1/7 * x2**7 - x2**3 + 0.5 * x2**2 - x2
    if y1 < y2:
        b = x2
        x2 = x1
        x1 = a + 0.382 * (b - a)
    else:
        a = x1
        x1 = x2 
        x2 = a + 0.618 * (b - a)

xm = (a + b) / 2
ym = 1/7 * xm**7 - xm**3 + 0.5 * xm**2 - xm
print("-----Answer-----")
print(xm)
print(ym)
print(counter)
