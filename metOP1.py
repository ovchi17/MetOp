a = 1
b = 1.5
e = 0.05
counter = 0
while True:
    counter += 1
    print("Шаг №" + str(counter))
    x1 = (a + b - e) / 2
    x2 = (a + b + e) / 2
    y1 = 1/7 * x1**7 - x1**3 + 0.5 * x1**2 - x1
    y2 = 1/7 * x2**7 - x2**3 + 0.5 * x2**2 - x2
    print(y1)
    print(y2)
    if y1 > y2:
        a = x1
    else:    
        b = x2
    if (b-a <= 2 * e):
        xMin = (a + b) / 2
        yMin = 1/7 * xMin**7 - xMin**3 + 0.5 * xMin**2 - xMin
        print(xMin)
        print(yMin)
        break
